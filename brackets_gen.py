# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 10:53:21 2021

@author: USER
"""

from itertools import permutations, combinations, count



def br_gen(n:int):
    """This function generates n pairs of correct brackets"""
    s='()'
    def gen_l(num):
        """Generates a list of brackets based on num"""
        st=list(permutations(n*s))
        l=[]
        for a in st:
            if a[0]!=s[1]:
                if a[-1]!=s[0]:    
                    l.append(list(a))
        return l
    
    

    li=gen_l(n)
    
    
    def checkbr(m:list):
        """This will validate the bracket correctness of the list elements and return the indexes
        of the validated ones"""
        ne=[]
        for net in m:
            ne.append(net)
        i = 1
        while i < len(ne):
            if ne[i]==s[1] and ne[i-1]==s[0]:
                ne.pop(i-1)
                ne.pop(i-1)
                i-=2
            i+=1
        return ne
    
    def unique(bon:list):
        """Searches and deletes duplicates from the list"""
        i=0
        while i < len(bon)-1:
            j=i+1
            while j<len(bon):
                if bon[i]==bon[j]:
                    bon.remove(bon[j])
                    j-=1
                j+=1
            i+=1
        return bon
                    
       
    final=unique(unique(li))
    for f in final:
        if checkbr(f)==[]:
            print(''.join(f))
        
    
    
    
       
       
    
    
    
      
    
        
    

   

        