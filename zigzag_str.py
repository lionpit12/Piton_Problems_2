# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:35:44 2021

@author: USER
"""

def zigzag(s:str, n):
    """This function will print out a string in a zigzag manner depending
    on the number of rows needed"""
    assert type(s)==str and type(n)==int, "Only strings and int allowed!"
    s=s.lower()
    result=[]
    for i in range(n):
        l=[' ']
        j=i
        if i==0 or i==n-1:
            while j<len(s):
                l[-1]=s[j]
                if j+(n-1)*2 < len(s):
                     l=l+[' ']*(n-1)
                j+=(n-1)*2
            result.append(l)
        else:
            while j<len(s):
                l[-1]=s[j]
                if j+(n-1)*2 < len(s):
                    l=l+[' ']*(n-1)
                    l[-1-i]=s[j+(n-1-i)*2]
                elif j+2*(n-1-i) < len(s):   
                    l=l+[' ']*(n-1-i)
                    l[-1]=s[j+(n-1-i)*2]
                j+=(n-1)*2
            result.append(l)
    for x in result:
        print(str(x).replace(',',''), end='\n')
                    
                    
                
            
        
            
        
            
                
          
                
                
                
                
                
                
         
   
        

    
        
                    
            
        
        
        
        
        
    