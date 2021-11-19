# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 08:06:36 2021

@author: USER
"""

def set_zero(l:list):
    """This function will turn to zeros same line and column where zero is found"""
    res=[]
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j]==0:
                res.append([i,j])
    for t in res:
        for jj in range(len(l[0])):
            l[t[0]][jj]=0
        for ii in range(len(l)):
            l[ii][t[1]]=0
                
    return l
    
        
             
    