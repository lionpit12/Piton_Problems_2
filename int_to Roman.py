# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 12:18:47 2021

@author: USER
"""

def toroman(n:int):
    """This functin converts integers to roman numbers and prints it out"""
    keys=[1,5,10,50,100,500,1000]
    values=['I','V','X','L','C','D','M']
    dico={k:v for k,v in zip(keys,values)}
    dico_1={k:v for k,v in zip(values,keys)}
    dico_3={8:'VIII',80:'LXXX',800:'DCCC'}
    assert type(n)==int, 'Only integers allowed'
    s=str(n)
    map_s=map(int,s)
    l=list(map_s)
    
    def est():
        """ This function breaks a digit into sum of 10 pow"""
        result=[]
        for k,m in zip(l,range(len(s)-1,-1,-1)):
            result.append(k*10**m)
        return result
    
    initial=est() # we have splitied n into products
    
    def conversion(s):
       """This function returns the list of components to be
       changed into roman digits"""
       r=[]
       if s==0:
           r.append(s)
           return r
    
       def min_dif(el):
           if el==0:
               return r
           m=[]
           for x in keys:
               m.append(abs(x-el))
           el=m[m.index(min(m))]  
           r.append(keys[m.index(el)])
           return min_dif(el)
       return min_dif(s)
   
    final_1=conversion(n) # converted the initial number into appr summs
   
    
    def final_d():
        fin=[]
        for element in initial:
            if element not in dico_3.keys():
                fin.append(conversion(element))
            else:
                fin.append(element)
        return fin
    
    final_2=final_d() # we have converted initial into sums of appr roman digits
    
    def roman_1():
        """This function compiles the first var of a roman digit"""
        sfinal=''
        for kt,g in zip(initial,final_2):
            if kt==g:
                sfinal+=dico_3[g]
            elif max(g)<=kt:
                for e in g:
                    if e!=0:
                        sfinal+=dico[e]
            else:
                top=-1
                while top >(-1)*(len(g)+1):
                    if g[top]!=0:
                        sfinal+=dico[g[top]]
                        top-=1
        return sfinal
    
    def roman_2():
        """This funciton compiles the second var of a roman digit"""
        sfinal_1=''
        sfinal_2=''
        if sum(final_1)>n:
            sums=[]
            i=0
            while sum(sums)<n:
                sums.append(final_1[i])
                i+=1
            for gip in range(len(sums[:-1])):
                sfinal_1+=dico[final_1[gip]]
            for bip in reversed(final_1[len(sums)-1:]):
                sfinal_2+=dico[bip]
        else:
            for dip in (final_1):
                sfinal_2+=dico[dip]
        return sfinal_1+sfinal_2
    
    
                        
    if len(roman_2())!=len(roman_1()):
        return print(f"Вариант №1:{roman_2()}, Вариант №2:{roman_1()}")
    else:
        return print(f"{roman_1()}")
            
    
        
        
        
        
    
   
    
    
        

   
        
    
        
        
        
                
            
            
        
    
        
        

        
            
    
        
    