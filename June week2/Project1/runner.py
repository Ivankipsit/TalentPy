"""
Create a python module calculator.py with class Calculator. The calculator class should have
functions add(x,y), sub(x,y), mul(x,y), div(x,y). Create another file python runner.py and import
calculator module here and call add, sub, mul and div functions.
"""

import calculator as calc
from fractions import Fraction

x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))

obj1 = calc.Calcuator(x,y)
print("\n--> sum of {} and {} = {}".format(x,y,obj1.add(x,y)))
print("--> difference of {} and {} = {}".format(x,y,obj1.sub(x,y)))
print("--> product of {} and {} = {}".format(x,y,obj1.mul(x,y)))
print("--> {} up on {} = {} 'or simply' {}".format(x,y,obj1.div(x,y),Fraction(x,y)))
