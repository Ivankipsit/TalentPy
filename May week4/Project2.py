"""
Write a list comprehension to find factorial of each numbers in a given list L if and only
if the numbers are even. For Example: If L = [1,2,3,4] then output should be [2, 24].
"""

def fact(a):
    factorial = 1
    for k in range(1,a + 1):
       factorial = factorial*k
    return factorial
      

def facteven(L):
    List1 = [i for i in L if i%2==0]
#    return List1
    List2 = [fact(j) for j in List1]
    return List2
        

L = list(map(int, input().split()))
print(facteven(L))