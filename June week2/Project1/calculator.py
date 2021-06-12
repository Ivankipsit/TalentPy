"""
Create a python module calculator.py with class Calculator. The calculator class should have
functions add(x,y), sub(x,y), mul(x,y), div(x,y). Create another file python runner.py and import
calculator module here and call add, sub, mul and div functions.
"""

class Calcuator:
    def __init__ (self,x,y):
        self.x = x
        self.y = y

    def add(self,x,y):
        #returns sum
        return x+y
    def sub(self,x,y):
        #returns difference
        return x-y
    def mul(self,x,y):
        #returns product
        return x*y
    def div(self,x,y):
        #returns quotient 
        return x/y