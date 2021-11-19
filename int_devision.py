# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:35:20 2021

@author: USER
"""

def int_div(m,n):
    """ This function makes an integer devision (m//n)"""
    assert type(m)==int and type(n)==int , 'Only ints allowed!'
    if n==0:
        raise ZeroDivisionError
    elif n==1:
        return m
    r=abs(m)
    p=abs(n)
    i=0
    while r>=p:
        r-=p
        i+=1
    if m<0 and n>0 or m>0 and n<0:
        return -i
    return i
        
    
    
    
    