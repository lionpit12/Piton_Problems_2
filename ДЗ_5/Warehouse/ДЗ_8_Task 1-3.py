# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 07:23:32 2021

@author: USER
"""

# Task No 1

import re

class Data(object):
    
    def __init__(self, date_s):
        self.date_s=date_s
    
    @classmethod
    def strtonum(cls,date_s):
        """ This function takes date in str format ('day-month-year') 
        and returns a tuple with numeric values of the given string"""
        s=date_s.split('-')
        if len(s) !=3:
            raise TypeError ('Wrong separator between numbers!')
        a,b,c=s
        return int(a), int(b), int (c)
    
    @staticmethod
    def validation(date_s):
        """ This method validates the allowed ranges of numbers entered as data. You
        should enter the data in str format (day,month,year)."""
        s=re.findall(r"\d+",date_s)
        if len(s)!=3:
            raise ValueError ('Wrong numbers for a date!!!')
        for a in s:
            if int(a[0])==0:
                raise ValueError ("Numbers in a date should not start from zero!")
        if int(s[1])>12:
            raise ValueError ('Month number should be less then or equal 12!!')
        if len(s[2])!=4:
            raise ValueError ('Enter 4 positive digits to represent a year number!')
        c_days={1:31,2:29, 3:30,4:31,5:30,6:31,7:30,8:31,9:30,10:31,11:30,12:31}
        if int(s[0])>c_days[int(s[1])]:
            raise ValueError ('Impossible number of days in this Month!')
        print('Your date seems to be fine!')
            
# Task No 2

class Zero_Dev_Err(Exception):
    
    def __init__(self,txt):
        self.txt=txt
        
    
def num_d():
    """ Two number (first/second) devision function"""

    try:
        m=int(input('Give me a number: '))
        n=int(input('Give me a number: '))
        if n==0:
            raise Zero_Dev_Err('You can not divide by zero!')
    except TypeError:
        print('Wrong data type!')
    except Zero_Dev_Err as err: 
        print(err)
    else:
        print(f'The division result is {m/n}')
    finally:
        print('Try one more time!')
        
# Task No 3

class OwnTypeError(Exception):
    
    def __init__(self,value):
        self.value=value
        
    def __str__(self):
        return repr(self.value)

# var 1
# def mylist():
#     """ This function creates a list comprised of numbers entered by the user. If not a number
#     is entered an Error will be raised, print 'stop' to quit."""
#     a=[]
#     try:
#         while True:
#             a.append(int(input('Enter one number now: ')))
#     except TypeError:
#         print('Wrong data type entered!')
#     finally:
#         return a
            
# var 2
def mylist():
    """ This function creates a list comprised of numbers entered by the user. If not a number
    is entered an Error will be raised, print 'stop' to quit."""
    a=[]
    while True:
        m=input('Enter a number now: ')
        if m=='stop':
            break
        try:
            if m.isdigit()==False:
                raise OwnTypeError(m)
        except OwnTypeError as err:
            print('Wrong data type entered',err.value)
        else:
            a.append(m)
    return a

# Task No 4


    
       
            
            
       
    
       
        
   
            
    
    
   
        
        