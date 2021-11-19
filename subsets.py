# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 10:03:35 2021

@author: USER
"""

def subsets(l:list):
    """This function returns all possible combinations of l. L contains unique
    integers"""
    
    def combinations(m,n:list,result=None, i=0):
        """This function retunrns m combinations from n"""
        # assert 0<m<=n, "m should be positive interger and less or equal n"
        source=n[i:]
        result=result or []
        if len(source)==m:
            result.append(source)
            return result
        j=1
        while j<len(source)-m+2:
            fin=[source[0]]
            for s in range(j,j+m-1):
                fin.append(source[s])
            if fin not in result:
                result.append(fin)
            j+=1
        i+=1
        return combinations(m,n,result,i)
    final=[]
    
    for num in range(1,len(l)+1):
        final.append(combinations(num,l))
    
    return print(sum(final, []))
        