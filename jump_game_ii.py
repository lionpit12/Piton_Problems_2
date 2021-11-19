# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 08:44:22 2021

@author: USER
"""


def jump(l:list):
    """This function returns the min number of jumps to reach the last
    index from the first index showing the track"""
    assert l[0]!=0, 'First el should not be zero!'

    ind=[0]
    i=0
    while i<len(l)-1:
        if ind[-1]+l[ind[-1]]>=len(l)-1:
            return print(f'You can jump {len(ind)} times as follows {[l[x] for x in ind]}')
        sums=[]
        inds=[]
        
        for j in range (i+1,i+1+l[i]):
            if l[j]==0:
                continue
            s=j+l[j]
            if s>=len(l)-1:
                ind.append(j)
                return print(f'You can jump {len(ind)} times as follows {[l[x] for x in ind]}')
            sums.append(s)
            inds.append(j)
           
        if sums==[]:
            return print('No jumps are possible in this list!')
        ind.append(inds[sums.index(max(sums))])
        i=inds[sums.index(max(sums))]
        
            
    
       
    
            
            
            
            
    
    
        
            
            
    
        
        
        
        
        
