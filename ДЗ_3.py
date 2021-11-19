# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:28:18 2021

@author: USER
"""

# Task No 1

def two_num_dev(a,b):
    """This function takes 2 numbers (a,b) and returns (a/b)"""
    
    try:
        return round(a/b,2)
    
    except ZeroDivisionError:
        
        print('You have given zero for denom, try again, punk!')
        
# Task No 2        

def print_data(Name='Ivan',Sirname='Petrov',BY=2001,
               Place='Moscow', email='abc@com.ru',phone=890808080808):
    
    """ This function prints the named parameters out"""
    
    print(f'Name: {Name}, Sirname: {Sirname}, Birth Year: {BY}, Place: {Place},email: {email},phone: {phone}')
          

# Task No 3

def my_func(a,b,c):
    """This function returns the sum of the two biggest args between a,b,c"""
    return max(a+b,b+c,a+c)

# Task No 4

# var 1 with **

def pow_func(x,y:int):
    """This function calculates positive x to the power of the whole y"""
    assert x>0 and type(y)==int
    try:
       return x**y
    except TypeError:
       print("Wrong input type")
   
# var 2 with * 

def pow_f(x,y:int):
    """This function calculates positive x to the power of the whole y"""
    assert x>0 and type(y)==int
    if y==0:
        return 1
    try:
        product=x
        i=abs(y)
        while i>1:
            product=product*x
            i-=1
        if y>0:
            return product
        else:
            return 1/product
    except TypeError:
        print("Wrong input type")      
    
# Task No 5

def num_sum():
    
    """ This function summs up the given numbers. Enter 's' to stop summation. """
    

    def input_d():
        s=input("Enter numbers separated by space. Type 's' to quit: ")
        s=s.split()
        return s
    
    try:
        summe=0
        while True:
            s=input_d()
            if 's' in s:
                s=s[:s.index('s')]
                a=[0]*len(s)
                for i in range(len(s)):
                    a[i]=int(s[i])
                return summe+sum(a)
            else:
                a=[0]*len(s)
                for i in range(len(s)):
                    a[i]=int(s[i])
                summe=summe+sum(a)
                print(summe)
            
    except TypeError:
        print('Wrong data type')
                
            
# Task No 6

def int_func(s:str):
    """ This function takes a word and returns it with capital letter"""
    return s.capitalize()
            
def cap_words():
    """This function takes words separated by space and returns them capitalized"""
    s=input('Enter some words, separated by space: ')
    s=s.split()
    for a in s:
        print(int_func(a), end=' ')
         

    
    
        
 
      
    
                
    
           
        
            
            
        
    
    
     
    
    
    

    
    