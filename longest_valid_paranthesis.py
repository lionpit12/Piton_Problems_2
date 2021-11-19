# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 08:24:00 2021

@author: USER
"""

def show_valbr(m:str):
        """This function will search and find all valid brackets in a str of
        brackets if there are any and will show them and calculate 
        their number"""
        s='()'
        ne=''
        match=[]
        for net in m:
            ne+=net
        i = 1
        while i < len(ne):
            if ne[i]==s[1] and ne[i-1]==s[0]: # braces are verified
                if i not in match and i-1 not in match:
                     match.append(i-1)
                     match.append(i)
            elif ne[i]==s[1] and ne[i-1]==s[1]: # goes backwards to check validity
                if i not in match and i-1 in match:
                    j=i-1
                    while j>=0:
                        if ne[j]==s[0] and j not in match:
                            match.append(j)
                            match.append(i)
                        j-=1   
            i+=1
        match=sorted(match) # print in right order
        # print(match)
        if match !=[]:
            if len(match)<len(m):
                print (f"The following {len(match)} brackets are valid:")
                for k in match:
                    print(m[k], end='')
            else:
                print ('Congrats, all brackets are valid, Pal!')
                print(m)
        else:
            print("No valid brackets discovered, sorry Pal!")
        
        
                    
                        
                    
                    
                    
    
                
            
                    
                    
                
            
        
