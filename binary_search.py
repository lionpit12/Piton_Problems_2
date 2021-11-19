# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 15:00:57 2021

@author: USER
"""

def bin_search(l:list, target:int):
    """ This function will search for all target elements in a list, will
    return the indexes of the first and last targets or [-1, -1] if the aren't any"""
    assert type(target)==int, 'Only ints allowed!'
    if l[0]>target or l[-1]<target:
        return (-1,-1)
    elif l[0]==target==l[-1]:
        return (0,len(l)-1)
    
    counter=0
    counter_1=0
    
    def searchleft(ll:list, t:int):
        """This function will search for the leftmost index of the target in
        the list"""
        nonlocal counter
        left=0
        right=len(ll)-1
       
        if ll[left]==t:
            return left
        if right-left==1:
            if ll[right]==t:
                return right+counter
            return -1
        middle=(right-left)//2
        if ll[middle]>=t:
            return searchleft(ll[:middle+1],t)
        else:
            counter+=middle-left
            return searchleft(ll[middle:],t)
        
    def searchright(li:list, ti:int):
        """This function will search for the rightmost index of the target in
        the list"""
        nonlocal counter_1
        lefto=0
        righto=len(li)-1
        
        if li[righto]==ti:
            return righto
        if righto-lefto==1:
            if li[lefto]==ti:
                return lefto+counter_1
            return -1
        mid=(righto-lefto)//2
        if li[mid]<=ti:
            counter_1+=mid-lefto
            return searchright(li[mid:],ti)
        else:
            return searchright(li[:mid],ti)
            
    a=searchleft(l,target)
    b=searchright(l,target)
    return(a,b)
   
    
   
       
    
            
            
            
        
        
        

        
    