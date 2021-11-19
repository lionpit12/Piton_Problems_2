# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:03:21 2021

@author: USER
"""
import re

def max_el_sum(l:list):
    """ This function returns the max sum of the elements in a list."""
    assert len(l)>0, "The list should contain at least 1 el!"
    if len(l)==1:
        return l[0]
    result=[]
    for m in l:
        if m>0:
            result.append(m)
    if len(result)!=0:
        return sum(result)
    else:
        if 0 in l:
            return 0
        else:
            return max(l)
        
def lastwordlen(s:str):
    """This function returns the length of the last word in a string"""
    assert type(s)==str, 'Only strings allowed!'
    result=[]
    m=re.findall(r"[\w']+|[.,!?;]", s)
    for x in m:
        if len(x)>1:
            result.append (x)
    return len(result[-1])

    
    
    

            
        