# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 08:32:13 2021

@author: USER
"""

def min_win(a:str,b:str):
    """This function searches for the minimum substring of a that has all of
    of the letters from b"""
    
    if len(a)<len(b):
        return None
    def find_all(aa:str, bb:str):
        c=[]
        for i in range(len(bb)):
            for j in range(len(aa)):
                if bb[i]==aa[j]:
                    if j not in c:
                        c.append(j)
                        break
                    continue
        return c
    # print (find_all(a,b))
    fin=[]
    final=[]
    for k in range(len(a)-len(b)+1):
        jj=k+len(b)
        while jj<=len(a):
            cc=find_all(a[k:jj],b)
            if len(cc)==len(b):
                final.append(a[k:jj])
                fin.append(len(a[k:jj]))
                break
            jj+=1
    mm=min(fin)
    # print(fin)
    result=[]
    for i in range(len(fin)):
        if fin[i]==mm:
            result.append(final[i])
    return result or None
            
        
            
            
    