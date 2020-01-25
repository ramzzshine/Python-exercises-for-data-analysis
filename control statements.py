# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:49:35 2020

@author: DS7_RVepuri
"""

''''write the syntax for if else statement'''

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
    
    
"""
Write a python program using if-else statement
"""

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
    
"""
write a python program using for loop.
"""

count = 0
while (count < 3):     
    count = count + 1
    print("Hello Geek")
    
"""
Write the syntax for loop
"""

    
for iterator_var in sequence:
    statements(s)
    
"""
Write the syntax for while statement
"""    
while expression:
    statement(s)
    
    
"""
Write a python program using While statement
"""   
    
  while (count < 3):     
    count = count + 1
    print("Hello Geek") 
else: 
    print("In Else Block") 
    
"""
write  the syntax for do while
"""
do {
     loop block
    } 
while (condition);:
    
"""
Write a python program using do while
"""

n = 10

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1   
print("The sum is", sum)

"""
Write  the syntax for break and continue
"""
 while (expression1) :
     statement_1 
     statement_2
     ......
     if expression1:
         continue
     if expression2 :
         break     
    
"""
Write a python program using break and continue
"""
num_sum = 0
count = 0
while(count<10):
    num_sum = num_sum + count
    count = count + 1 
    if count== 5:
        break
print("Sum of first ",count,"integers is: ", num_sum)


for x in range(7):
    if (x == 3 or x==6):
        continue
    print(x)
    
"""Write the program for pass statement"""
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass