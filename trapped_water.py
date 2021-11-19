# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:31:32 2021

@author: USER
"""

# Trapping water

def tr_w(l:list):
    """This function calculates the possible volume of the trapped
    water between two obstacles(non zero values of the list)"""
    
    volume=0
    i=0
    while i<len(l)-1:
        if l[i]>l[i+1]:
            j=i+1
            diff=[]
            
            while len(l[j:])>0:
          
                delta=l[i]-l[j]
                diff.append(delta)
                if delta<=0:
                    break
                j+=1
            if diff[-1]<=0:
                volume+=sum(diff[:len(diff)-1])
                i+=len(diff)-1
            elif diff.count(min(diff))==1:
                for x in diff:
                    if x==min(diff):
                        i+=diff.index(min(diff))
                        break
                    volume+=x-min(diff)
            elif 1<diff.count(min(diff))<len(diff):
                for xx in range(len(diff)-1,-1,-1):
                    if diff[xx]==min(diff):
                        for tt in diff[:xx]:
                            volume+=tt-min(diff)
                        i+=xx+1
                    
    
        i+=1
        
    return print(f'You have {volume} cubic meter of the trapped water!')
            
        