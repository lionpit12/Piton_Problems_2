# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:58:10 2021

@author: USER
"""

def waterpool(l:list):
    """This function finds max container volume from a list of heights,
    the index diff is the container width"""
    result=[]
    for i in range(len(l)-1):
        j=i+1
        while j<len(l):
            result.append(min(l[i],l[j])*(j-i))
            j+=1
    print(result)
    return max(result)
        
        
    