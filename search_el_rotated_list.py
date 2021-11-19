# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:46:38 2021

@author: USER
"""

def get_index(a:list, m:int):
    """This function returns the m index of the previously rotated
    ascending list of ints if the m is present and -1 if not"""
    f=[]
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            f=a[i+1:]+a[:i+1]
            break
    
    r=[]
    def search_el(l:list,el:int):
        """ THis function searches for an el in a list of sorted ints and returns
        the index of the first found el or its possible index if el is not found"""
        right=len(l)
        left =0
        middle=(right-left)//2
        r.append(l[middle])
        if middle<1:
            return -1
        if l[middle]==el:
            return print(f'Yes el is found, its index is {middle}')
        elif l[middle]>el:
            search_el(l[:middle],el)
        else:
            search_el(l[middle:],el)
            
    
    search_el(f,m)
                   
                 
    
            
   
        
    