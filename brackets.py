# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:09:38 2021

@author: USER
"""

 
br=["(","{","[",")","}","]"]
ml='(),[],{},({[()]})'

def find_b(s:str):
    result=[]
    for el in s:
        if el in br:
            result.append(el)
    return result

def check(l):
    """THis function validates the correctness of brackets"""
    s1=0
    s2=0
    if l[0] in br[3:] or l[-1] in br[:3]:
            return print('Brackets non validated')
    for el in l:
        if el in br[:3]:
            s1+=1
        elif el in br[3:]:
            s2+=1
    
    if s1!=s2:
        return print('Brackets non validated')
    
    i = 1
    while i < len(l):    
        if l[i] in br[3:] and l[i-1]==br[br.index(l[i])-3]:
            l.pop(i-1)
            l.pop(i-1)
            i-=2
        i+=1
    if l==[]:
        print('Congrats! Brackets in this string are all validated!')
    else:
        print('Brackets are non validated, these brackets are unmatched: ', l)
     
  
            
      
        
   
         
        
