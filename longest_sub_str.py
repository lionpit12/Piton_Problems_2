# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:19:06 2021

@author: USER
"""


def lonsubstr(s:str):
    
    """This function returns the longest substring of a string s without
    repeating characters.If s is an empty str, it will return 0"""
    
    assert type(s)==str, "Only strings allowed!"
    if len(s)<=1:
        return 0
    result=[]
    for i in range(len(s)):
        if i==len(s):
            result.append(1)
            return s[result.index(max(result)):result.index(max(result))+max(result)]
        st=s[i]
        j=0
        while j<len(s[i+1:]) and s[j+i+1] not in st:
            st=st+s[j+i+1]
            if len(st)==len(s[i+1:]):
                result.append(len(st))
                return s[result.index(max(result)):result.index(max(result))+max(result)]
            j+=1
        result.append(len(st))
    
   
        
       
    
    
 
        

           
            
        
            
      
    
        