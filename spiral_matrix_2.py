# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:53:43 2021

@author: USER
"""

def spir_2(n:int):
    """This function will generate matrix n x n and will fill it in a spriral
    order clockwise"""
    
    mrx=[[0]*n for i in range(n)]
    seq=[i for i in range(n**2)]
    ind=list(range(n))
    
    def sp(a:list, ind, num=0):
        """This function will fill in the els from list a into list b in a sprial
        order clockwise"""
        nonlocal mrx
        if len(ind)<1:
            return print (mrx)
      
        ni=len(ind)
        for i in range(ni):
            mrx[num][num+i]=a[i]
        a=a[ni:]
        
        f=len(mrx[num+1:-1-num])
        for x,k in zip(mrx[num+1:-1-num],range(f)):
            x[-1-num]=a[k]
        a=a[f:]
        
        for j in range(ni):
            mrx[-1-num][-1-num-j]=a[j]
        a=a[ni:]
        ff=len(range(-2-num,-ni,-1))
        for xx,kk in zip(range(-2-num,-ni-1,-1),range(ff)):
            mrx[xx][0+num]=a[kk]
        a=a[ff:]
        
        inds=ind[1:-1]
        nums=num+1
        
        sp(a,inds,num=nums)
        
    sp(seq,ind)
    
        