# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 09:41:31 2021

@author: USER
"""

def word_search(l:list, word:str):
    """This function will return True and the position of letters 
    if the word is found and False if the word is not found"""
    
    result=[]
    for k in range (len(word)):
        fin=[]
        for i in range(len(l)):
            for j in range(len(l[0])):
                if l[i][j]==word[k]:
                    fin.append((i,j))
       
        result.append(fin)
    
    # print(result)
    if len(result)<len(word):
        return False
    
    final=[]
    def search_sec(li=result[0],res=None,i=1):
        """This function will search for a right sub sequence of letters"""
        if i==len(result):
            return res
        res=res or []
        for x in li:
            lis=[]
                
            for y in result[i]:
                if (y[0]==x[0] and abs(y[1]-x[1])==1 or y[1]==x[1] and abs(y[0]-x[0]==1)) and y not in res:
                    if x not in res:
                        res.append(x)
                    res.append(y)
                    lis.append(y)
                    i+=1
                    return search_sec(lis,res,i)
    return search_sec() or False
    
                    
                    
                    
       
                    
                    
                
            
        
            
            