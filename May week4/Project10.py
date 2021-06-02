"""
Write a generator which can give random values every time.
"""
import random as rd
def GeneratorFun():
    yield rd.randint(-10000,10000)
for _ in GeneratorFun(): 
    print(_)
