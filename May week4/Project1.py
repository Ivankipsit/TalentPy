"""
Create a lambda function which takes two inputs X and Y and performs X power Y
operation and returns the output. For Example: If X is 2 and Y is 3, then 2 power 3 = 2
* 2 * 2 = 8.
"""
x = input().split()
y = input().split()
X = [int(a) for a in x]
Y = [int(a) for a in y]
print(X)
print(Y)
new_list = []
lam_obj = list(map(lambda X,Y: X**Y, new_list))
print(new_list)
