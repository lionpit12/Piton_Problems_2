# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:38:45 2021

@author: USER
"""

def edit_d(a:str,b:str):
    """This function will find the longest common sequence of letters as
    it is in b"""
    
                
                    
    def carcass(l,m,result=None):
        """This function seeks carcass of m in l and returns it"""
        res=result or []
        for i in range(len(m)):
            for j in range(len(l)):
                if m[i]==l[j]:
                    res.append(m[i])
                    if j+1<=len(l)-1 and i+1<=len(m)-1:
                        return carcass(l[j+1:],m[i+1:],res)
                    return res
        return res
    
    fin=[]
    for k in range(len(b)):
        r=carcass(a,b[k:])
        if r not in fin:
            fin.append(r)
    # print (fin)
    length=[]      
    
    for x in fin:
        a=len(x)
        length.append(a)

    mm=max(length)
    
    for xx in fin:
        if len(xx)==mm:
            print (xx)
            
    
    
        
        
            
    
                
        
    
    
        