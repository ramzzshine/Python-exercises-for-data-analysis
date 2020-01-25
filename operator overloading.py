# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:24:55 2020

@author: DS7_RVepuri
"""

# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading. 

class A: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b
      

	# adding two objects 
	def __add__(self, other): 
		return self.a + other.a, self.b + other.b
   # adding two objects 
	def __sub__(self, other): 
		return self.a - other.a, self.b - other.b 
   # adding two objects 
	def __mul__(self, other): 
		return self.a * other.a, self.b * other.b 
   # adding two objects 
	def __mod__(self, other): 
		return self.a % other.a, self.b % other.b 
   # adding two objects 
	def __pow__(self, other): 
		return self.a ** other.a, self.b ** other.b 

	def __str__(self): 
		return self.a, self.b 

Ob1 = A(1, 2) 
Ob2 = A(2, 3) 
Ob3 = Ob1 + Ob2 
Ob4 = Ob1 - Ob2
Ob5 = Ob1 * Ob2
Ob6 = Ob1 % Ob2
Ob7 = Ob1 ** Ob2
print(Ob3) 
print(Ob4)
print(Ob5)
print(Ob6)
print(Ob7)

# Python program to overload equality, less than, greater than operators 

class A: 
	def __init__(self, a): 
		self.a = a 
	def __lt__(self, other): 
		if(self.a<other.a): 
			return "ob1 is lessthan ob2"
		else: 
			return "ob2 is less than ob1"
        
	def __eq__(self, other): 
		if(self.a == other.a): 
			return "Both are equal"
		else: 
			return "Not equal"
   def __gt__(self,other):
       if (obj1>obj2):
           print("obj is greater than obj2")
       else:
           return "obj2 is greater than obj2"
        
   
ob1 = A(2) 
ob2 = A(3) 
print(ob1 < ob2) 

ob3 = A(4) 
ob4 = A(4) 
print(ob1 == ob2) 

ob1 = A(2) 
ob2 = A(3) 
if(ob1>ob2): 
	print("ob1 is greater than ob2") 
else: 
	print("ob2 is greater than ob1") 


