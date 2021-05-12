"""
You are going to design a magical calculator with the following functions.
• Function that takes input and calculates it’s factorial. (A)
• Function that takes input and calculate it’s sum of digits. (B)
• Function that takes input and find’s the largest digit in the input. (C)
- Implement all the above functions.
- Get input and pass the input to factorial function (A), get the output from
factorial function and pass it as input to sum of digits function (B). Get the output
from sum of digits function, add the output with random 5 digit number and pass
the outcome to largest digit function (C) and print the output that you receive from
function C.
Sample I/O:
• Input 5
• Output of A = 120
• Output of B(120) = 1+2+0 = 3
• Output of C(3 + 10000 = 10003) = 3 (Here 10000 is the random number)
• Hence output is 3 , where 3 is the largest digit of 10003.
"""

import random

def factorial(a):
    list1 = []
    for i in range(1,a+1):
        list1.append(i)
    fact = 1
    for i in list1:
        temp = i
        fact = i * fact
    return fact
    
def sumofDig(a):
    sum = 0
    while a > 0 :
        temp = a%10
        sum += temp
        a //= 10
    return sum
    
def bigDig(a):
    list1 = []
    list2 = []
    a = str(a)
    list1 = list(a)
    for ele in list1:
        k = int(ele)
        list2.append(k)
    return(max(list2))
a = int(input("Enter: "))
print(bigDig(sumofDig(factorial(a))+random.randint(9999,100000)))