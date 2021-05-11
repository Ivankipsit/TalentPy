"""
John would like to create a function to check whether given number is
positive or negative or neutral. Help him to write an independent function
and pass different inputs to the function and check its behaviour.
"""

def check(a):
    if (a > 0):
        return  "Positive."
    if (a < 0):
        return  "Negative."
    if (a == 0):
        return  "Neutral."
a = eval(input())
print(check(a))