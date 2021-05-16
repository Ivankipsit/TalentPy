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
    