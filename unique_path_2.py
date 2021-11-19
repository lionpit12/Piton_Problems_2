# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:45:47 2021

@author: USER
"""

def unique_path_2(board:list):
    """This function returns the number of paths to reach the right lower square of
    the m x n matrix excluding the obstacles noted as 1 in the matrix"""
    
    m=len(board)
    n=len(board[0])
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j]==0:
                board[i+1][j+1]=board[i][j+1]+board[i+1][j]
                break
            if board[i+1][j+1]!=0:
                board[i+1][j+1]=board[i][j+1]+board[i+1][j]
        
    return board[m-1][n-1]