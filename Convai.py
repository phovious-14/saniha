# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 07:19:34 2022

@author: samay
"""
from bot import ask



import wikipedia #pip install wikipedia



from text_clean import clean

def chate(x):
    msg = clean(x)
    
    if "age" in msg:
        res = "I will turn 21 next year"
        print(res)
        flag = 1
        return(res)

        
    elif "old" in msg:
        res = "i am 20 years old"
        print(res)
        flag = 1
        return(res)

    
    elif "birthday" in msg:
        res = "my birthday is on 21st april"
        print(res)
        flag = 1 
        return(res)

        
    elif "search" in msg:
        print('Searching Wikipedia...')
        res = msg.replace("search", "")
        res = wikipedia.summary(res, sentences=2)
        print(res)
        flag = 1
        return(res)
    
    
    elif msg != '':
        res = ask(msg)
        print(res)
        return(res)
   
        

if __name__ == '__main__':
   pass