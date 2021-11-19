# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 07:31:35 2021

@author: USER
"""
from abc import ABC, abstractmethod


# Task No 1

class Matrix(object):
    
    def __init__(self, list_of_lists):
        for i in range(len(list_of_lists)-1):
            if len(list_of_lists[i])!=len(list_of_lists[i+1]):
                raise ValueError ('All members of the list should have equal length!')
        self.list_of_lists=list_of_lists
        
    def get_Matrix(self):
        return list(self.list_of_lists)
        
    def __add__(self,other):
        l=self.get_Matrix()
        m=other.get_Matrix()
        assert len(l)==len(m)
        new_list=[]
        for i in range(len(l)):
            if len(l[i])!=len(m[i]):
                raise ValueError ('The matrix should be of equal size!')
            for j in range(len(l[0])):
                new_list.append(l[i][j]+m[i][j]) # summation of the list el
        result=[new_list[i:i+len(l[0])] for i in range(0,len(new_list),len(l[0]))] # transform in list of lists
        return Matrix(result)
    
    def __str__(self):
        s=''
        for el in self.get_Matrix():
            s=s+str(el)[1:-1]+'\n'
            s=s.replace(',','')
            
        return s
        
        
# Task No 2

class Garment (ABC):
    def __init__(self, param):
        self.param=param
        
    @abstractmethod
    def material_u():
        pass
    
    
class Coat(Garment):
    
    def __init__(self, V):
        self.V=V
        
    @property   
    def volume (self):
        return self.V
    
    def  __str__(self):
        return f'Coat, size= {self.volume}'
        
    def material_u(self):
        v=self.volume
        assert type(v)==int or type(v)==float
        return round(v/6.5 + 0.5, 2)
        
class Suit(Garment):
    def __init__(self,H):
        self.H=H
    @property     
    def height(self):
        return self.H
    
    def  __str__(self):
        return f'Suit, height= {self.height}'
        
    def material_u(self):
        h=self.height
        assert type(h)==int or type(h)==float
        return round(2*h + 0.3)      
    
# Task No 3

class Cell(object):
    def __init__(self, num):
        assert type(num)==int
        self.num=num
        
    def get_cell(self):
        return self.num
    
    def __add__(self,other):
        new_cell=self.num + other.num
        return Cell(new_cell)
    
    def __sub__(self, other):
        s=self.num-other.num
        if abs(s)>0:
            return s
        raise ValueError ('The Cell quantity difference should be more then zero!')
        
    def __mul__(self,other):
        return Cell(self.num*other.num)
    
    def __truediv__(self,other):
        return Cell(self.num//other.num)
    
    def __str__(self):
        return f"Cell object, cell numbers = {self.num}"
    
    def make_order(self, cell_per_row):
        n_cells=self.get_cell()
        num1=n_cells//cell_per_row
        rem=n_cells%cell_per_row
        s=''
        a=0
        while a<num1:
            s=s+'*'*cell_per_row +'\n'
            a+=1
        if rem !=0:
            s=s+'*'*rem +'\n'
        return s.replace("''", '')
        
        
        
        

    
    
        


        


        
        
            
        
        
        
         