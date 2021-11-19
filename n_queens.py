# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:48:42 2021

@author: USER
"""

board=[["."]*4 for i in range(4)]
def queens(board):
    """This function returns the allowed positions of the queens on the nxn board"""
    
    
    result=[]
    finall=[]
    
    def final(a:tuple,board:list,forbidden=None):
        
        """This function returns the list with Queen placed on the original board"""
           
        if len(board)==0:
            return finall
        i,j=a
        allowed=[]
        forbidden=forbidden or []
        
        
        ii=i+1
        while ii<len(board[0]):
            forbidden.append((ii,j))
            ii+=1
        
        k,z=i+1,j+1
        while z<len(board[0]):
            forbidden.append((k,z))
            k+=1
            z+=1
        l,s=i+1,j-1
        while s>-1:
            forbidden.append((l,s))
            l+=1
            s-=1
            
        for m in range(len(board[0])):
            if (i+1,m) not in forbidden and i+1<len(board[0]):
                allowed.append((i+1,m))
        # print(allowed)
        # print(forbidden)
        for x in allowed:
            finall.append(x)
            final(x,board[i+1:],forbidden)
            
    
    # for cols in range(len(board)):
    #     finall.append((0,cols))
    #     final((0,cols),board)
        
        
       
        
    return finall
    
   
      

            
                
          
        
        
            
        
   
        
            
            
        
                
        
       
        
        
    
    
        
        
        
   