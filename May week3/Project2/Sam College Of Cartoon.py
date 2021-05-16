import random
def Function1(*a): 
    if list1 == [""]:
        return False
    else:
        n = random.randint(0,len(list1))
        return list1[n]
def Function2(F1):
    if F1 == False:
        return False
    else:
        return F1.swapcase()        
def Function3(F2,M=3):
    return F2*M
def main(*a,M=3):
    if Function2((Function1(list1))) == False:
        print("Oops! No cartoon Selected.")
    else:
        print(Function3((Function2((Function1(list1)))),M))
list1 = input().split(",")
M = input()
if M == "":
    main(list1)
else:
    M = int(M)
    main(list1,M)