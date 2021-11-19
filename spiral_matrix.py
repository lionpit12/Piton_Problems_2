# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 09:29:55 2021

@author: USER
"""

def spiralm(l:list,result=None):
    """THis function returns the matrix el in a spiral order clockwise"""
    
    result=result or []
    if len(l)==1:
        for x in l[0]:
            result.append(x)
        return print(result)
    elif len(l)==2:
        for xx in l[0]:
            result.append(xx)
        for i in range(-1,-len(l[1])-1,-1):
            result.append(l[1][i])
        return print(result)
    
    for el in l[0]:
        result.append(el)
        
    for ele in l[1:-1]:
        result.append(ele[-1])
    
    for ind in range(-1,-len(l[-1])-1,-1):
        result.append(l[-1][ind])
        
    for ix in range(-2,-len(l),-1):
        result.append(l[ix][0])
        
    s=[]
    for tt in l[1:-1]:
        s.append(tt[1:-1])
        
    spiralm(s,result)
        
        
    
        
        
        

    
    
    