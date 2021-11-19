# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:35:06 2021

@author: USER
"""

def insert_int(a:list, b:list):
    
    """This function inserts b in a, if overlapped it will merge overlapping regions"""
    
    if a==[]:
        return [b]
    
    if a[-1][1]<b[0]:
        a.append(b)
        return a
        
    if a[-1][0]<=b[0]:
        if a[-1][1]>=b[1]:
            return a
        
        result=[]
        result.append(a[-1][0])
        result.append(b[1])
        a.pop()
        a.append(result)
        return a  
    
    
    
    ind=0                        # determine the index of insertion
    for k in range(len(a)):
        if a[k][0]>b[0]:
            if k!=0:
                if a[k-1][1]>=b[1]:
                    return a
            ind+=k
            a.insert(ind,b)
            break
        elif a[k][0]==b[0]:
            if a[k][1]>=b[1]:
                return a
            res=[]
            res.append(a[k][0])
            res.append(b[1])
            ind+=k
            a.insert(ind,res)
            a.pop(ind+1)
            break
    
   
    if ind!=0 and a[ind-1][1]>=a[ind][1]:
        a.pop(ind)
        return a
    
    i=ind+1
    while i < len(a):
        if a[i][0]>a[ind][1]:
            break
        r=[]
        if a[i][1]>a[ind][1]:
            r.append(a[ind][0])
            r.append(a[i][1])
            a.insert(ind,r)
            a.pop(i)
            a.pop(i)
            break
        
        else:
            a.pop(i)
            i-=1
        i+=1
       
    if a[ind-1][1]>=a[ind][0]:
        re=[]
        re.append(a[ind-1][0])
        re.append(a[ind][1])
        a.insert(ind-1,re)
        a.pop(ind)
        a.pop(ind)
          
    return a
   
            
            
            
            