"""
Be Positive!  Create a function to sum up all positive argument inputs. Inputs ranges from 0 to N,
where N can be any positive number.
"""

def sumof(*a):
    a = []
    for ele in list1:
        if ele > 0:
            a.append(ele)
        else:
            continue
    return sum(a)
N = input("Enter inputs with space in between them: ").split()
list1 = []
for i in N:
    k = int(i)
    list1.append(k)
print(sumof(list1))
