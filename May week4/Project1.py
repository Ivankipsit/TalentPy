"""
Create a lambda function which takes two inputs X and Y and performs X power Y
operation and returns the output. For Example: If X is 2 and Y is 3, then 2 power 3 = 2
* 2 * 2 = 8.
"""
X = int(input())
Y = int(input())
lam_obj = lambda X, Y: X ** Y
print(f"{X} power {Y} = {lam_obj(X,Y)}")
