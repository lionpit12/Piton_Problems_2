# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 19:57:36 2021

@author: USER
"""

# Task No 5,6
Printers={}
Scaners={}
Xeroxes={}
i=0
j=0
k=0
A={}
B={}
C={}

from Classes import Printer,Scaner,Xerox,ProductClassError

def store(class_object):
    """ This method takes home electronics products and stores them accordingly"""
    global i
    global j
    global k
    global Printers
    global Scaners
    global Xeroxes
    m=[Printer,Scaner,Xerox]
    
    if type(class_object) not in m:
        raise ProductClassError ('Wrong Product Type!!!')
      
    try:
        product=class_object.get_product()
        
    except ProductClassError:
        print("Wrong Product Type!!!")
   
    
    if product=='printer':
        
        producer=class_object.get_producer()
        price=class_object.get_price()
        origin=class_object.get_origin()
        size=class_object.get_size()
        
        Printers[f'printer{i}']=[producer,price,origin,size]
        i+=1
       
        
    elif product=='scaner':
        
        producer=class_object.get_producer()
        price=class_object.get_price()
        origin=class_object.get_origin()
        size=class_object.get_size()
        
        Scaners[f'scaner{j}']=[producer,price,origin,size]
        j+=1
        
        
    elif product=='xerox':
         
         producer=class_object.get_producer()
         price=class_object.get_price()
         origin=class_object.get_origin()
         size=class_object.get_size()
         is_multicolor=class_object.is_multicolor()
         is_wifi=class_object.is_wifi()
        
         Xeroxes[f'xerox{k}']=[producer,price,origin,size,is_multicolor,is_wifi]
         k+=1
         
    if Printers:
        return Printers
    elif Scaners:
        return Scaners
    elif Xeroxes:
        return Xeroxes
    else:
        return None
        
def move(product,warehouse=A):
    """ This method moves goods from the main storage of Printers, Scaners and 
    Xeroxes to the A,B or C warehouses"""
    global A
    global B
    global C
    assert warehouse==A or warehouse==B or warehouse==C
    
    if product in Printers:
        warehouse[product]=Printers.pop(product)
        
        
    elif product in Scaners:
        warehouse[product]=Scaners.pop(product)
        
    elif product in Xeroxes:
        warehouse[product]=Xeroxes.pop(product)
        
    else:
        print("Product not found. Check the spelling and try again!")
        
    return warehouse  
        
        