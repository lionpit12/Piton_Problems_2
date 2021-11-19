# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:41:39 2021

@author: USER
"""

def text_just(l:list, limit:int):
    """This function will justify the words according to the defined limit"""
    
    
    for x in l:        # delete too big a list member
        if len(x)>limit:
            l.remove(x)
    result=[]
    counts=0
   
    while counts<len(l):
        
        final=''
        i=0
        i+=counts
        k=limit
        while k>0:
            k-=len(l[i])
            if k<0:
                if i>0:
                    i-=1
                break
            elif k==0:
                break
            k-=1
            if k==0 or i==len(l)-1:
                break
            i+=1
        print(i)
        if counts==i:
            final+=l[counts]
            final+=' '*(limit-len(l[i]))
            result.append(final)
            if i==len(l)-1:
                    break
            counts=i+1
        elif counts==i+1:
            final+=l[counts]+' '*(limit-(len(l[counts])+len(l[i])))+l[i]
            result.append(final)
            if i==len(l)-1:
                break
            counts=i+1
        else:
            l_sum=0
            for j in range(counts,i+1):
                l_sum+=len(l[j])
                # print (l_sum)
            delta=limit-l_sum
            just=delta//(i-counts)
            for t in range(counts,i-1):
                final+=l[t]
                final+=' '*just
                delta-=just
            final+=l[i-1]+' '*delta
            final+=l[i]
            result.append(final)
            if i==len(l)-1:
                break
        
        counts=i+1
        
    return result