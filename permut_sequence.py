# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 07:32:30 2021

@author: USER
"""
def enum_perm(n:list,m):
    """This function will generate permutations of n and return the m th one"""
    assert 0<m<len(n), "m should be positive and less then the length of the list"
    a=[]
    def gen_permutations(l:list, prefix=[]):
        """THis function generates permutations of the list els and returns them"""
       
        # prefix=prefix or []
        if len(prefix)==len(l):
            a.append(list(prefix))
            return a
            
        
        for i in range(len(l)):
            if l[i] in prefix:
                continue
            prefix.append(l[i])
            gen_permutations(l,prefix)
            prefix.pop()
            
    gen_permutations(n)
    
    
    print(f'you have the following permutations: {a}, m_th element is {a[m-1]}')
