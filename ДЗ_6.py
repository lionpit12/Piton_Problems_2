# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 08:09:26 2021

@author: USER
"""

# Task No 1

import time
import random

class Trafficlight(object):
    def __init__(self,color):
        if color not in ('red','yellow','green'):
            raise ValueError ('You can enter only red, yellow or green')
        self._color=color
    
    def running(self):
        
        c={'red':7,'yellow':2, 'green':10}
        color=self._color
        # if color not in c.keys():
        #     raise ValueError ('You have entered wrong color, the color should be red, yellow or green')
        
        while True:
            if color =='red':
                print(f"Be prepared to enter 'yellow' in {c['red']} sec")
                time.sleep(c['red'])
                color=input("Enter 'yellow' now: ")
                if color !='yellow':
                    print('Wrong color entered. Try again later.')
                    break
            elif color=='yellow':
                print(f"Be prepared to enter 'green' in {c['yellow']} sec")
                time.sleep(c['yellow'])
                color=input("Enter 'green' now: ")
                if color !='green':
                    print('Wrong color entered. Try again later.')
                    break
            else:
                print(f"Be prepared to enter 'red' in {c['green']} sec")
                time.sleep(c['green'])
                color=input("Enter 'red' now: ")
                if color !='red':
                    print('Wrong color entered. Try again later.')
                    break
        
           
# Task No 2

class Road(object):
    
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
        
    
    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width
        

    def mass_a(self,thickness,mass):
        l=self.getLength()
        w=self.getWidth()
        return l*w*thickness/1000*mass
    
# Task No 3

class Worker(object):
    

    def __init__(self, name, sirname, position, income:tuple):
        self.name = name
        self.sirname = sirname
        self.position = position
        self.__income = {'wages':income[0],'bonus':income[1]}
    
        
    def getIncome(self):
        return self.__income

class Position(Worker):
           
    def get_full_name(self):
        return self.name, self.sirname
    
    def get_total_income(self):
        return sum(self.getIncome().values())
    
# Task No 4

class Car(object):
    
    def __init__(self, color, name, is_police=False):
              
        self.color = color
        self.name = name
        self.is_police=is_police
    
    def go(self):
        print('The car is moving now!')
        
    def stop(self):
        print('The car has pulled over.')
    
    def turn_right(self):
        print('Ther car has turned right.')
        
    def turn_left(self):
        print('The car has turned left.')
    
    def show_speed(self):
        return random.randint(0,100)
        
        
class SportCar(Car):
    
    def show_speed(self):
        return random.randint(150,250)

class TownCar(Car):
    
    def show_speed(self):
        x=random.randint(30,80)
        if x>60:
            print(f'Slow down baby, you drive at {x} km per hour in a town!!!')
        else:
            print(f'You drive at {x} km per hour. That a boy!!')
            
            
class WorkCar(Car):
    
    def show_speed(self):
        return random.randint(20,50)
    
class PoliceCar(Car):
    
    def __init__(self,color,name,is_police=True):
        super().__init__(color,name,is_police)
        
        
# Task No 5

class Stationary(object):
    def __init__(self,title):
         self.title=title
         
    def draw(self):
        print('Drawing starts now.')
        
class Pencil(Stationary):
    
    def draw(self):
        print('Drawing with pencil is cool, but not long lasting!')
        
class Pen(Stationary):
    
    def draw(self):
        print('Check your pen for ink before getting started.')
        
class Handle(Stationary):
    
    def draw(self):
        print('Be careful while drawing with your Handle.')
    
     
     
         
         
    
         
    
        
        
        
            

    
   

        
        

    
    
    

    
    
    
        
    
    
    
    
    
   
        
    
        