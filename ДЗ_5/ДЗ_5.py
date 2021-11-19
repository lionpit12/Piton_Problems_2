# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 07:16:28 2021

@author: USER
"""
import functools
import json
import random
import re



# Task No 1

def write_f():
    """ You can write something in a newly created file"""
    def takein():
        a=[]
        while True:
            b=input("Type smth now, to quit type space: ")
            if len(b)==0:
                break
            a.append(b)
        return a
    
    with open("Text.txt", 'w') as f:
        t=takein()
        for txt in t:
            f.writelines(f'{txt} \n')
        
# Task No 2

            

def count(file_n):
    """ This function calculates the number of rows and number of chars in each row in a file"""
    def open_f():
        try:
            with open(file_n,'r') as f:
                data=[]
                for t in f.readlines():
                    data.append(t)
                return data
        except IOError:
            print("File not found, try agein!")   
            
    l=open_f()
    for row, el in enumerate(l):
        print(f'row {row} contains {len(str(el).split())} word(s)')
    return row+1
        
    
 # Task No 3
 # Работает только с такой записью в Тext.txt: Фамилия(стринг) зарплата(число)
 
def sal_ev(file_n):
     """ This function reads info (Sirname salary) from a file and computes average"""
     try:
         with open (file_n,'r') as f:
             l=f.read().splitlines()
             try:
                 dico={str(x).split()[0]:str(x).split()[1] for x in l} #creates dict
                 values=list(dico.values())
                 numbers=[int(i) for i in values]
                 av=functools.reduce(lambda a,b:a+b, numbers)/len(numbers)
                 print(f'Average salary is {av:.2f} dollars')
                 print ("These employees have a salary less then 20000 dollars:")
                 for key in dico:
                     if int(dico.get(key))<20000:
                         print (key)
             except ValueError:
                 print ("Wrong value in the file")
     except IOError:
         print('File not found, try again!')

# Task No 4

def rw(file_n):
    """This function opens a count eng file changes words eng to rus and writes new lines in a new file"""
    with open (file_n, 'r') as f, open('Test_2.txt','w') as t:
        r=f.readlines()
        for x in r:
            print(x)
        f.close()
        t.writelines("один-1\n два-2\n три-3\n четыре-4\n" )
     
             
# Task No 5

def read_n():
    """This programm creates a file with a list of numbers and then computes it"""
    with open('Numbers.txt','w') as f:
        f.write('1 2 3 4 5 6 7 88 99 66 1 34 5')
    with open('Numbers.txt','r') as f:
        l=str(f.readline()).split()
        m=[]
        for x in l:
            m.append(int(x))
        summe=sum(m)
        print(f'The following nums {l} are in the file, their summ is  {summe}')
        #print(l,type(l))
        
# Task No 6

def data_d(file_n):
    """ This function reads the file and returns the dictionary whith the hour total"""
    try:
        with open (file_n,'r') as f:
            l=f.read().splitlines()
            try:
                dico={str(x).split(':')[0]:str(x).split()[1:] for x in l} # made dict from input
                for k in dico.keys():
                    dico[k]=re.findall("\d+",str(dico[k])) # numbers filtered
                    dico[k]=[int(i) for i in dico[k]] # converted to ints
                    dico[k]=functools.reduce(lambda a,b:a+b, dico[k]) # summmation
                return dico
            except ValueError:
                print("Wrong value in the file")
    except IOError:
        print('No such file found, try again!')
    
        
# Task No 7

def av_profit(file_n):
    """This function reads a file with data and return dict with analytics"""
    try:
        with open (file_n,'r') as f:
            l=f.read().splitlines()
            try:
                dico={str(x).split()[0]:str(x).split()[1:] for x in l}
                for k in dico.keys():
                    dico[k]=re.findall("\d+",str(dico[k])) # numbers filtered
                    dico[k]=[int(i) for i in dico[k]]
                    dico[k]=functools.reduce(lambda a,b:a-b, dico[k]) # summmation
                profit=0
                # profit=[dico[k] for k in dico if dico[k]>0]
                for k in dico:
                    if dico[k]>0:
                        profit+=dico[k]
                av_profit=profit/len(dico)
                dico_p={'Average profit':av_profit}
                print(f'Companies profit is: {dico}')
                print(f'{dico_p}')
                #data=json.dumps(dico)
                # return data
            except ValueError:
                print("Wrong value in the file")
                    
        
    except IOError:
        print('No such file found, try again!')
                
           
           
              
               
    
                
              
    
    
        
         
     
         
         
                        
        
         
         
     
             
             
              
            
     
            
    
     
     
     
            
             
             
   
        
    
  
     
    
            
 