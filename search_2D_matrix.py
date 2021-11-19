# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 07:34:33 2021

@author: USER
"""
m=[]
def search_el(l:list,el:int):
    """ THis function searches for an el in a list of sorted ints and returns
    the index of the first found el or its possible index if el is not found"""
    right=len(l)
    left =0
    middle=(right-left)//2
    m.append(l[middle])
    if middle<1:
        return print(f'No, el is not found, its index could be {m[-1]}')
    if l[middle]==el:
        return print(f'Yes el is found, its index is {middle}')
    elif l[middle]>el:
        search_el(l[:middle],el)
    else:
        search_el(l[middle:],el)


def search_2d(l:list,a:int):
    """THis function makes an efficient search of an integer (a) in a sorted 2D Matrix
    and returns True or False depending on the result"""
    m=len(l)
    n=len(l[0])
    if a<l[0][0] or a>l[m-1][n-1]:
        return False
    i=m//2
    while -1<i<m:
        if a<l[i][0]:
            i-=1
        elif a>l[i][n-1]:
            i+=1
        else:
            return search_el(l[i],a)
                