# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 08:43:51 2021

@author: USER
"""

# Task No 1

A=[2,'Hi',(2,3,4),{1,2,3},[0,0,0],1==1,{'banana':1,'apple':2},(None)]

def check_type(A):
    """ This function checks the el type of the list A"""
    for index, el in enumerate(A):
        print(index, type(el))


# Task No 2

def swap_listel():
    """This function swaps two neighbouring els a list. If len of the list is odd, last el remains on its place"""
    
   
    
    def make_list():
        A=[]
        while True:
            a=input('Enter the el of the list, type -1 to end: ')
            a=convert_input(a)
            if a == -1:
                break
            A.append(a)
        print('You have created the following list: ', A)
        print ('The swaped version of your list is: ', swap(A))
        
    def convert_input(input):
        try:
            # Convert it into integer
            val = int(input)
        except ValueError:
            val=input
        finally:
            return val
    
    
    def swap(A):
        
        if len(A)%2==0:
            for i in range(0,len(A)-1,2):
                A[i],A[i+1]=A[i+1],A[i]
        else:
            for i in range(0,len(A)-2,2):
                A[i],A[i+1]=A[i+1],A[i]
        return A
        
    make_list()
    swap(A) 
    
# Task No 3
# var 'List'

def season_time():
    """This function returns the season depending on the Month number"""
    def season(i):
         if i==0:
             return "Winter"
         elif i==1:
             return "Spring"
         elif i==2:
             return "Summer"
         else:
             return "Autumn"
    
    M=[{12,1,2},{3,4,5},{6,7,8},{9,10,11}]
    a=int(input('Enter the number between (incl) 1 and 12: '))
    
    try:
        for i in range(4) :
            if a in M[i]:
                print (f'{a} corresponds to {season (i)}') 
                return
    except ValueError:
        print("This is not a number or not a number")
    else:
        print('Your number does not match any season. Try again')
        
# var 'Dictionary'

def season_t():
    """This function returns the season depending on the Month number"""
    M={'Winter':(12,1,2),
       'Spring':(3,4,5),
       'Summer':(6,7,8),
       'Autumn':(9,10,11)}
    a=int(input('Enter the figure between (incl) 1 and 12: '))
    
    if a in M['Winter']:
        print(f'Your number corresponds to Winter')           
    elif a in M['Spring']:
        print(f'Your number corresponds to Spring')
    elif a in M['Summer']:
        print(f'Your number corresponds to Summer')
    elif a in M['Autumn']:
        print(f'Your number corresponds to Winter')   
    else:
        print('No match to any season, try again')
        
# Task No 4

def handle_str():
    """This function prints words from the string you give on new line with numeration"""
    string=input('Enter your string: ')
    string=string.split()
    for index, el in enumerate(string):
        print(index,el[:11])
            
    
# Task No 5

def rating():
    """ THis function returns the rating list based on the number given."""
    
    
    final=[7,5,3,3,2]   
    while True:
        a=int(input('Enter the natural number, type -1, 0 to quit: '))
        if a== -1 or a==0:
            print('Your rating list is', final)
            break
        a=abs(a)   
        i=0
        while i<len(final) and a<=final[i]:
            i+=1
        final.insert(i,a)

# Task No 6- С этим заданием у меня возникли сложности! 
# В виду повышения сложности заданий, наверно имеет смысл сократить количество
# иначе зашьемся))

def data_st():
    """This function structures your input data"""
    final=[]
    
    def enter_data():
        print("Enter the product,price,quantity and units.")
        print("To quit entering data type'stop'.")
        try:
            while True:
                product=input('Enter the product: ')
                price=int(input('Enter the price: '))
                quantity=int(input('Enter the quantity: '))
                unit=input('Enter the units (ex:pcs): ')
                data=[product,price,quantity,unit]
                if 'stop' in data:
                    print("You have entered 'stop' to finish entering data")
                    break
                final.append(data)
        except ValueError:
            print('Wrong data type entered. Start entering again by calling data_st function')
        finally:
            print('You have entered the following data', final)
            print('Which could be structured as follows: ')
            return final
      
    def transform_d(final):
        data=('product','price','quantity','unit')
        w_list=final
        middle=[0]*(len(w_list)-2)
        for i in range (len(w_list)-2):
            middle[i] =list(zip(data,w_list[i]))
            middle.insert(i,middle[i])
            #dico=dict(middle)
        #print('You have got the following data structure: ', middle)
        for index, el in enumerate(middle):
            print("\n",index, el)
        #print('Which can be transformed into dictionary', dico)
    
    enter_data()
    transform_d(final)
            

        
        
            
            
                
                
                    
                
                
    



        

    

                
    
            
        

        
    
            
        
    
        
   

     
          
        