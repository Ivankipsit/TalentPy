"""
Star Generation: Create a python function which takes a number N and generates following star
pattern accordingly. N ranges from 1 to any positive number.  Make sure if N is not passed as
argument while calling function, it should take 3 as it’s default value.
"""


def star(N = 3):
    for _ in range(1,N+1):
        if _%2 == 0:
            print("@"*_)
        else:
            print("*"*_)
N = input()
if N == "":
    star()
else:
    N = int(N)
    star(N)
    