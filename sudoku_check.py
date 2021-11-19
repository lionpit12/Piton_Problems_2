# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:52:42 2021

@author: USER
"""

import random
import re

def gen_sudoku(n):
    """This function will generate random n elements(numbers) in 0-9 range for the
    sudoku table"""
    assert type(n)==int and 0<n<=81, "Only positive ints not greater than 81 allowed!"
    ab=[["."]*9 for i in range(9)]
    rows=[]
    columns=[]
    for i in range(n):
        rows.append(random.randint(0,8))   
        columns.append(random.randint(0,8))
    for m,n in zip(rows,columns):
        ab[m][n]=str(random.randint(0,9))
        
    return ab
        
def check_sudoku(a:list):
    """This function will prove if the sudoku is correct: no repeating els in
    rows and columns, no repeating els in 3x3 squares"""
    c='0123456789'
    trans=[[a[i][j] for i in range(9)] for j in range(9)]
    
    
    for x,y in zip (a,trans):
        t_1=re.findall(r"\d", str(x))
        t_2=re.findall(r"\d", str(y))
        if len(t_1)!=len(set(t_1)) or len(t_2)!=len(set(t_2)):
            return print("Sudoku is not valid, try again.")
        
    def check_sq(a,k,t,nr=3,nc=3):
        """This function will check for the uniqness of els in
        sxp dimensional square"""
        nonlocal c
        result=[]
        for i in range(t,t+nc):
            for j in range(k,k+nr):
                if a[i][j] in c:
                    result.append(a[i][j])
        if len(result)==len(set(result)):
            return True
        return False
    
    for k in range(0,len(a),3):
        for t in range(0,len(a),3):
            if not check_sq(a,k,t):
                return print("Sudoku is not validated!")
    
    
    return print("Huray! Sudoku is valid!!!")
    
    
            
    