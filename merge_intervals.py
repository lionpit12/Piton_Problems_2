# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 13:07:30 2021

@author: USER
"""

def merge_intervals(l:list):
    
    """This function merges overlapping intervals from the list and returns the result"""
    a=[]
    for x in l:
        a.append(x)
    
    i=0
    while i<len(a)-1:
        merge=[]
        if a[i][1]>=a[i+1][0]:
            merge.append(a[i][0])
            merge.append(a[i+1][1])
            a.insert(i,merge)
            a.pop(i+1)
            a.pop(i+1)
            i-=1
        i+=1
        
    return print(f'if you merge els of {l} you will get {a}')
            