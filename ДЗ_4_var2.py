# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 07:56:43 2021

@author: USER
"""

# Task No 1


#from sys import argv 
#script_name, hours, rate, bonus=argv
#salary = hours*rate + bonus
#print(salary)


# Task No 2

def my_list(A:list):
    """This function returns the list of elements which are bigger then the preceding ones 
    of the original list"""
    return [A[i+1] for i in range(len(A)-1) if A[i+1]>A[i]]


# Task No 3

def dev_times2021():
    """This function returns numbers which a devisable by 20 or 21 from the
    list between 20 and 240"""
    return [num for num in range(20,240) if num%20==0 or num%21==0]

# Task No 4

def unique_num(A:list):
    """This function returns a list of the unique elements of the original list"""
    try:
        return [A[i] for i in range (len(A)) if A.count(A[i])==1]
    except TypeError:
        print('Wrong type, body!')
        
# Task No 5



def even_num():
    """THis function returns the list of even numbers starting from 100 till
    1000 including and calculates the product of all elements of the list"""
    from functools import reduce
    lis=[k for k in range(100,1001) if k%2==0]
    print(lis, end=' ')
    return reduce(lambda a,b:a*b,lis)
        
# Task No 6

# sub Task a
def gen_whole_num(a,b):
    """ This function generates b whole numbers starting from a whole number a."""
    assert type(a)==int and type(b)==int
    from itertools import count
    m=count(a,1)
    count=0
    while count<b:
        print(next(m))
        count+=1
   
            
# sub Task b

def cycle_list(A:list,b:int):
    """ This funcition repeats the elements of the list A, b times"""
    from itertools import cycle
    count=0
    m=cycle(A)
    while count<b:
        print(next(m))
        count+=1
        
    
# Task No 7

def fuc(n):
    """This function computes n!"""
    from functools import reduce
    assert n>=0
    lis=[i for i in range(1,n+1)]
    if n==0:
        yield 1
    else:
        fuctorial=reduce(lambda a,b:a*b,lis)
        yield fuctorial



