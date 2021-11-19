# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 12:33:58 2021

@author: USER
"""

def lsubpol(s:str):
    """ The function will return the longest polidrom substring of a string s"""
    
    def polisubs(a:str):
        for i in range(len(a)//2):
            if a[i]!=a[-i-1]:
                return -1
        return a
        
    k=len(s)
    while k>1:
        j=0
        while j<=len(s)-k:
            m=polisubs(s[j:j+k])
            if m!=-1:
                return m
            j+=1
        k-=1
     
            
            
            
        
        