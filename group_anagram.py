# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:33:18 2021

@author: USER
"""



def group_an(l:list):
    """This function returns the grouping of the anagram words if there are any"""
    a=[]
    
    def gen_permutations(l:list, prefix=None):
        """THis function generates permutations of the list els and returns them"""
        nonlocal a
        prefix=prefix or []
        if len(prefix)==len(l):
            a.append(list(prefix))
            return
    
        for i in range(len(l)):
            if l[i] in prefix:
                continue
            prefix.append(l[i])
            gen_permutations(l,prefix)
            prefix.pop()
    
    result=[]
    for i in range(len(l)):
        gen_permutations(l[i])
        m=[]
        for x in a:
            if ''.join(x) not in m:
                m.append(''.join(x))
        result.append(m)
        a.clear()
    final=[]
    for x in result:
        if sorted(x) not in final:
            final.append(sorted(x))
    answer=[]        
    for t in final:
        fin=[]
        for s in t:
            if s in l and s not in fin:
                fin.append(s)
        answer.append(fin)
            
                
    return answer
   
    
    
    
    