"""
Mr.Talentpy would like to create a function one_or_eight which takes an integer input (no) and
performs following operation.
1. Square the number if it is single digit. (Eg: 3, then 3 * 3 = 9)
2. If it is not single digit, square each digits and add. (Eg: 12, then (1*1) + (2*2) = 1+4 = 5
You have to repeat step (1) and (2) until you reach 1 or 89. Note that, always your result will reach
1 or 89 for sure. Input must be a positive number.
If the operation reaches at the end, 89 return True, if operation reaches 1 at the end return False.
"""


def one_or_eight(no):
    list1 = []
    list2 = []
    list3 = []
    while ((no != 89) or (no != 1)):
        no = str(no)
        list1 = list(no)
        for ele in list1:
            k = int(ele)
            list2.append(k)
        for elem in list2:
            elem = elem**2
            list3.append(elem)
        no = sum(list3)
#        print("list1=",list1)
        list1.clear()
#        print("list2=",list2)
        list2.clear()
#        print("list3=",list3)
        list3.clear()
#        print(no)
        if no == 89:
            return True
            break
        if no == 1:
            return False
            break

no = int(input())
if no > 0:
    print(one_or_eight(no))
else:
    print("Please enter a positive number.")