# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 09:28:21 2021

@author: USER
"""
from functools import lru_cache # a decorator function

def steps(n):
    """ The function calculates the number of combinations to reach an n th step
    if you move from the first step by one or by two step move"""
    final =[0,1]+[0]*(n-1)
    for i in range (2, n+1):
        final[i]=final[i-1]+final[i-2]
    return final[n]
    
result={}
def fib_dic(n):
    """ Calculate fib num with the help of a dic"""
    if n in result:
        return result[n]
    if n ==1:
        value=1
        
    elif n==2:
        value=1
        
    elif n>2:
        value=fib_dic(n-1)+fib_dic(n-2)
    
    result[n]=value
    return value


@lru_cache(maxsize=1000)
def fib(n):
    assert type(n)==int and n>0, "Only positive integers allowed!"
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)