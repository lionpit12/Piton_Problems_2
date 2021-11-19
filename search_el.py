# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 09:00:23 2021

@author: USER
"""
m=[]
def search_el(l:list,el:int):
    """ THis function searches for an el in a list of sorted ints and returns
    the index of the first found el or its possible index if el is not found"""
    right=len(l)
    left =0
    middle=(right-left)//2
    m.append(middle)
    if middle<1:
        return print(f'No, el is not found, its index could be {m[-1]}')
    if l[middle]==el:
        return print(f'Yes el is found, its index is {m[-1]}')
    elif l[middle]>el:
        search_el(l[:middle],el)
    else:
        search_el(l[middle:],el)
    


            
        
        
