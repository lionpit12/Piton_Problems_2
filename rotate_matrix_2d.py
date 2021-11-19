# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 09:59:14 2021

@author: USER
"""

def matrix_rotation(m:list):
    """This functions rotates els of the matrix on 90 degrees"""
    trans=[[m[i][j] for i in range(len(m))] for j in range(len(m))] # transponieren die Matrix
    for x in trans:
        for k in range(len(x)//2):
            x[k],x[-1-k]=x[-1-k],x[k]
    return trans
            
    
    
        
        
        
           
            
   
        
        
            
        
            
    
            