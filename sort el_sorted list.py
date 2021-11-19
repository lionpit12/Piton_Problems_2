# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 12:53:49 2021

@author: USER
"""

def opt(a):
    
    """This function sorts the unique list elements of the sorted list at its 
    beginning"""
    i=0
    while a[i]<=a[i+1] and i<len(a)-1:
        if a[i]==a[i+1]:
            tmp=a[i+1]
            for k in range(i+1,len(a)-1):
                a[k]=a[k+1]
            a[len(a)-1]=tmp
            i-=1
        i+=1
    return a