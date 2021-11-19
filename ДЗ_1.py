# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:24:52 2021

@author: USER
"""
# Task No 2
def change_sec():
    """This function takes the seconds value as int and returns the minutes,hours value as int in formant hh:min:sec """
    
    seconds=int(input('Please enter the number of seconds to convert, punk: '))
    assert type(seconds)==int
    minutes=seconds//60
    hours=minutes//60
    
    print(f'{seconds} seconds make hh:min:sec-{hours} : {minutes} : {seconds}')
    
# Task No 3

def crazy_sum():
    """ This function makes a summation of n, nn, nnn in base 10 metric sys"""
    
    n=int(input('Just gimme a number, punk: '))
    assert 0<=n<=9 
    nn=n*10+n
    nnn=nn*10+n
    print('Ur crazy summ, punk, equals to  ' + str(n+nn+nnn))
    
# Task No 4

def biggest_num(n):
    """ This funcion takes a no less then two-digit integer ans shows which digit of it is the greatest"""
    assert type(n)==int and abs(n)>9
    sn=str(n)
    ln=[0]*len(sn)
    for i in range (len(ln)):
        ln[i]=int(sn[i])
    print(f'from the given number n biggest number is- {max(ln)}')
    
# Task No 5

def economics():
    """This function computes your past period performance result"""
    sales=int(input('Enter your sales for the past period: '))
    costs=int(input('Enter your costs for the past period: '))
    profit=sales-costs
    print(f'Your profit for the period is {profit} dollars')
    if profit>0:
        print(f'Your rate of return for the period is {profit/sales*100:.2f} %')
        n_workers=int(input('Enter the number of employees: '))
        print(f'Your profit per capita is {profit/n_workers:.2f} dollars')
    else:
        print('Bad times Fella, but dont give up!')
        
           
# Task No 6

def training_progress(a,b,c):
    """This programm calculates your progress in achieving your target (b kilometers) starting from (a kilometers) with (c) daily progress """
    assert 0<c<=100
    current=a
    target=b
    progress=current*c/100
    num_days=0
    while target>current:
        print(f'Today you ran {current:.2f} km')
        current=current*(1+progress)
        num_days +=1
    print("You need", num_days, " days to reach your target of", b, "Kilometers per day")
        
# Additional

def train_squat(a,b,c):
    """This programm calculates your progress in achieving your target (b squats) starting from (a squats) with (c) daily progress """
    current=a
    target=b
    progress=c
    num_days=0
    while target>current:
        print(f'Today you squat {current} squats')
        current=current + progress
        num_days +=1
    print("You need", num_days, " days to reach your target of", b, "squats per day")
        
        