# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:20:22 2021

@author: USER
"""



def gen_permutations(l:list, prefix=None):
    """THis function generates permutations of the list els and returns them"""
    prefix=prefix or []
    if len(prefix)==len(l):
        return print(prefix)
    
    for i in range(len(l)):
        if l[i] in prefix:
            continue
        prefix.append(l[i])
        gen_permutations(l,prefix)
        prefix.pop()
    