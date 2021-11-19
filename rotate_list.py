# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:25:05 2021

@author: USER
"""

def rot_l(l:list,k:int):
    """This function will rotate elemenets of list for k steps"""
    
    rotations=k%len(l)
    if rotations==0:
        return l
    
    store=[]
    for x in l[-rotations:]:
        store.append(x)
    
    for j in range(-rotations-1,-len(l)-1,-1):
        l[j+rotations]=l[j]
      
    for k in range(len(store)):
        l[k]=store[k]
        
    return l
    
