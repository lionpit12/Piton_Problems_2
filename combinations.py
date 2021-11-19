# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 18:19:10 2021

@author: USER
"""

def combinations(m,n,result=None, i=1):
    """ This function returns combinations on m numbers in [1,n] range"""
    assert 0<m<=n, "m should be positive interger and less or equal n"
    source=[k for k in range (i,n+1)]
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
        
    
        
    
        
    
    
    
    