# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:06:37 2021

@author: USER
"""

from itertools import combinations

def sum_3(l:list):
    """This function takes in a list of integers or floats and picks up
    any 3 num combinations which sum is zero"""
    assert type(l)==list, 'Only list type of obects allowed'
    for el in l:
        assert type(el)==int or type(el)==float, 'The list should contnain only ints or floats'
    s=[]
    for b in combinations(l,3):
        if sum(b)==0:
            s.append(b)
    return s or None
            
        