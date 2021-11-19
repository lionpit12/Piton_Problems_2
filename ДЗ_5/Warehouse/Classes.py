# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:56:57 2021

@author: USER
"""
# Task No 4

class My_warehouse(object):
   
    
    @classmethod
    def warehouse(cls,length,width,height):
        return cls(length,width,height)
    
class Electronics(object):
    """Bacis class"""
    
    def __init__(self, product, producer, price, origin):
        
        self.product=product
        self.producer=producer
        self.price=price
        self.origin=origin
        
    def get_product(self):
        return self.product
    
    def get_producer(self):
        return self.producer
    
    def get_price(self):
        return self.price
    
    def get_origin(self):
        return self.origin
    
    
    def __str__(self):
        return (str(self.product)+':'+ str(self.producer)+':'+ 
                str(self.price)+'USD'+ ':'+ str(self.origin))



class Printer(Electronics):
    
    def __init__(self, product, producer, price, origin, size):
        super().__init__(product,producer,price,origin)
        self.size=size
        
    def __str__(self):
        return (str(self.product)+':'+ str(self.producer)+':'+ 
                str(self.price)+'USD'+':'+ str(self.origin))
    
    def get_size(self):
        return self.size
        
                
    
class Scaner(Electronics):
    def __init__(self, product, producer, price, origin, size):
        super().__init__(product,producer,price,origin)
        self.size=size
        
    def get_size(self):
        return self.size
    
    def __str__(self):
        return (str(self.product)+':'+ str(self.producer)+':'+ 
                str(self.price)+'USD'+ ':'+str(self.origin))

class Xerox(Electronics):
    
    def __init__(self, product, producer, price, 
                 origin, size, multicolor=True, wifi=True):
        super().__init__(product,producer,price,origin)
        
        self.size=size
        self.multicolor=multicolor
        self.wifi=wifi
    def get_size(self):
        return self.size
    
    def is_multicolor(self):
        return self.multicolor
    
    def is_wifi(self):
        return self.wifi
  
    
    def __str__(self):
        return (str(self.product)+':'+ str(self.producer)+':'+ 
                str(self.price)+'USD'+ ':'+
                str(self.origin)+ ':'+'Multicolor'+'-' +
                str(self.multicolor) +':''Wifi'+ '-' + str(self.wifi))
    

class ProductClassError(Exception):
    pass

# Task No 7

class ComplexNum(object):
    
    def __init__(self,a=0,b=0):
        """ This method creates a complex number (a+ib) from the given a,b"""
        self.a=a
        self.b=b
        
    def __str__(self):
        if self.a!=0 and self.b!=0:
            return str(self.a)+'+''i'+str(self.b)
        elif self.a==0 and self.b!=0:
            return 'i'+str(self.b)
        elif self.a!=0 and self.b==0:
            return str(self.a)
        else:
            return 0
                           
    
    def __add__(self, other):
        new_a=self.a+other.a
        new_b=self.b+other.b
        return ComplexNum(a=new_a,b=new_b)
    
    def __mul__(self, other):
        new_a=self.a*other.a-self.b*other.b
        new_b=self.a*other.b+self.b*other.a
        return ComplexNum(a=new_a,b=new_b)
        
        
    
    
        
        