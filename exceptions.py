# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:15:06 2020

@author: DS7_RVepuri
"""

"""Write the syntax for try-finally block."""
try: 
    k = 5//0 # raises divide by zero exception. 
    print(k) 
  
# handles zerodivision exception     
except ZeroDivisionError:    
    print("Can't divide by zero") 
      
finally: 
    # this block is always executed  
    # regardless of exception generation. 
    print('This is always executed')  

"""Write a python program for except clause with exception.
"""

import sys
ram = ['a',2,0]
for x in ram:
    try:
        print("The Entry Is",x)
        r = 1/int(x)
        break
    
    except:
        print("OOps",sys.exc_info()[0],"Occured")
        print("Next Entry")
        print()
    
    finally:
        print("this is from FInally")




""" Write a python program for except clause with multiple exception"""


import sys
try:
    d = 8
    d = d + '5'
except(TypeError, SyntaxError)as e:
    print (e)
    
    
    
"""Write a python program for raising an exception using raise clause"""
"""Write a python program for custom exceptions."""
try :  
    a = 3
    if a < 4 : 
  
        # throws ZeroDivisionError for a = 3  
        b = a/(a-3) 
      
    # throws NameError if a >= 4 
    print ("Value of b = ", b)
  
# note that braces () are necessary here for multiple exceptions 
except(ZeroDivisionError, NameError): 
    print ("\nError Occurred and Handled")
    
    
"""Write a python program for user defined exceptions."""

#!python
# define your own exceptions
class NumberTooSmallError(Exception):pass
 
class NumberTooBigError(Exception):
    message = '\nException: NumberTooBigError:\nYour number is too big. \nTry a smaller one!'
 
class NumberThreeError(Exception):
    def __init__(self):
        print ('\nException: ThreeNumberError:\nThree is not number ya\'re lookin\' for.\n')
 
class NumberFiveError(Exception):pass #uncaught exception
 
 
#function that uses user-defined exceptions
def checkNumber(num):
    if(num == 3):
        raise NumberThreeError
    elif(num == 5):
        raise NumberFiveError
    elif(num < 99):
        raise NumberTooSmallError
        print("Exception: given number is too small")
    elif(num > 99):
        raise NumberTooBigError
        print("Exception: given number is too big")
    return num
 
 
#python try...catch block (why it is called try...except?)
while 1:
    try:
        usrInput = int(input( "\nPlease enter the magic number: " ))
        print(usrInput)
        checkNumber(usrInput)
    except NumberTooSmallError:
        print ("Number too small")
    except NumberTooBigError as e:
        print ("Number too big" + e.message)
    except NumberThreeError:
        print ('Ooops!')
    #here shuld be one more except block for catching
    #int(): val is not numeric exception
    #except ValueError:
        #print "Only numeric values are accepted" 
    else:
        break
    