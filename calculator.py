# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:12:34 2020

@author: DS7_RVepuri
"""

class calculator:
    def __init__(self,*val):
        self.val = val
    def add (self):
        arg=0
        for i in self.val:
            arg+=i
        return arg
    def sub(self):
        arg=self.val[0]*2
        for i in self.val:
            arg-=i
        return arg
    def multiply(self):
        arg = 1
        for x in self.val:
            arg = arg*x
        return arg 
    def division(self):
        result = self.val[0]**2
        for x in self.val:
            result = result/x
        return result
    
calci = calculator(2,2,5,4,5)
print(calci.val)
print(calci.add(),calci.sub(),calci.multiply(),calci.division())
    

