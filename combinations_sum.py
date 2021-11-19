# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:21:19 2021

@author: USER
"""
#VAR 1 using substraction

def comb_sum(li:list,target:int):
    """ This function will chow all possible combinations of the a els
    to sum up to the given target"""
    
    assert target>0, "Only positive ints allowed!"
    a=sorted(li)
    result=[]
    dico={}
    for x in a:
        if x<2:
            return print ('Sorry, a list must contain pos ints greater than one only, try again later!')
        elif x>target:
            continue
        
        dif=target-x # checking if x==result
        if dif==0:
            x=x,
            result.append(list(x))
            continue
        j=1
        while dif>0:
            res2=[]
            if dif in a:
                i=j
                while i>0:
                    res2.append(x)
                    i-=1
                res2.append(dif)
            if sorted(res2) not in result and res2!=[]:
                result.append(sorted(res2))
            j+=1
            dif=dif-x
            
    for xx in a: # check if els may add up to the target
        if xx > target:
            continue
        su=[xx]
        temp=xx
        ii=0
        while ii<len(a) and sum(su)<=target:
            if sum(su)==target and sorted(su) not in result:
                result.append(sorted(su))
                break
            if temp!=a[ii]:
                delta=target-sum(su)
                if delta in a:
                    su.append(delta)
                    if sorted(su) not in result and sum(su)/len(su)!=temp:
                        result.append(sorted(su))
                        break
                su.append(a[ii])
            ii+=1
            
            
    return result or []   
            
            
        
# VAR 2 using devision
    
    # for c in range (-1,-len(a),-1):
    #     dev=[]
    #     d=c
    #     while d>-len(a):
    #         if a[c]%a[d-1]==0:
    #             dev.append(a[d-1])
    #         d-=1
    #     if dev:
    #         dico[a[c]]=dev
    # print(dico)
            
    # for x in a:
        
        
    #     if x>target:
    #         continue
    #     res=[]
        
    #     r=divmod(target,x)
    #     if r[0]<1:
    #         continue
    #     elif r[1]==0:
    #         res=[]
    #         i=0
    #         while i<r[0]:
    #             res.append(x)
    #             i+=1
    #         result.append(res)
          
            
    #     elif r[1] in a:
    #         res_2=[]
    #         j=0
    #         while j<r[0]:
    #             res_2.append(x)
    #             j+=1
    #         res_2.append(r[1])
    #         result.append(res_2)
          
    #     else:
    #         continue
        
    # if result:
    #         for f in result:
    #             for xx in f:
    #                 if xx in dico.keys():
    #                     for val in dico[xx]:
    #                         rr=[]
    #                         mm=0
    #                         while mm<xx/val:
    #                             rr.append(val)
    #                             mm+=1
    #                         rr.append(sum(f)-sum(rr))
    #                         if rr not in result:
    #                             result.append(rr)
    
            
    # return sum(result,[]) or []
        
        