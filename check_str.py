# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 10:24:41 2021

@author: USER
"""

def check(s:str,m:str):
    """This function tests whether there is a match of str m with str s, returns
    the index of the beginnig letter if positive, -1 if negative,0 if s is empty"""
    assert len(m)<=len(s), 'len of s shoulb be greater or equal to len of m!'
    if len(s)==0:
        return 0
    s=list(s)
    m=list(m)
    a=len(s)-len(m)
    result=[]
    i=0
    while i<a:
        k=0
        while k<len(m):
            if s[k]!=m[k]:
                break
            elif k==len(m)-1:
                result.append(m.index(m[0])+i)
            k+=1
        tmp=s[0]
        for j in range(len(s)-1):
            s[j]=s[j+1]
        s[len(s)-1]=tmp
        i+=1
    if len(result)==0:
        return -1
    else:
        return result
                
                
                
            