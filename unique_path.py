# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:29:37 2021

@author: USER
"""

def unique_path(m:int,n:int):
    """This function returns the number of paths to reach the right lower square of
    the m x n matrix"""
    board=[[1]*n for i in range(m)]
    for i in range(m-1):
        for j in range(n-1):
            board[i+1][j+1]=board[i][j+1]+board[i+1][j]
    return board[m-1][n-1]



            