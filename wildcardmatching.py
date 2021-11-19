# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:29:25 2021

@author: USER
"""

def wildcard(m:str,n:str):
    """ This function will see if the m and n match. If speical 
    characters are in n, it will take them into consideration"""
    if len(n)>len(m):
        return False
    ml=list(m)
    nl=list(n)

    # transform lists according to the special characters
    if '?' in nl:
        ind=nl.index('?')
        nl[ind]=ml[ind]
    if '*' in nl:
        indo=nl.index('*')
        if indo==len(nl)-1:
                nl=nl[:indo]+ml[indo:]
        elif indo==0 and len(nl)==1:
            nl=ml
        else:
            if nl[indo+1] in ml:
                nl=ml[:ml.index(nl[indo+1])]+nl[indo+1:]
    if len(ml)!=len(nl):
        return False
    for xx,yy in zip(ml,nl):
        if xx!=yy:
            return False
        return True
                
            
                
            
   
  
    
            
            