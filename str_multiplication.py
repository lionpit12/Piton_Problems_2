# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 12:15:29 2021

@author: USER
"""

def str_mlt(a:str, b:str):
    """This function takes to strings and returns their product as str"""
    nums='0123456789'
    aa=[ord(x)-48 for x in a if x in nums]
    bb=[ord(y)-48 for y in b if y in nums ]
    
    def make_num(l:list):
        """This function will compile a number from the list of ints"""
        pw=len(l)-1
        number=0
        for i in range(pw,-1,-1):
            number+=l[i]*10**(pw-i)
        return number
    
    def int_to_list(m:int, n=10):
        
        """ This function breaks a digit into sum of n pow"""
        result=[]
        while m>0:
            result.insert(0,m%n)
            m//=n
        return result
        
    aaa=make_num(aa)
    bbb=make_num(bb)
    product=aaa*bbb

    cc=int_to_list(product)
    if '-' in a and '-' not in b or '-' in b and '-' not in a:
        final_str='-'
    else:
        final_str=''
    for el in cc:
        final_str+=(chr(el+48))
    return final_str
    
    