"""
Mr.Talentpy would like to create a func,on one_or_eight which takes an integer input (no) and
performs following opera,on.
1. Square the number if it is single digit. (Eg: 3, then 3 * 3 = 9)
2. If it is not single digit, square each digits and add. (Eg: 12, then (1*1) + (2*2) = 1+4 = 5
You have to repeat step (1) and (2) until you reach 1 or 89. Note that, always your result will reach
1 or 89 for sure. Input must be a posi,ve number.
If the opera,on reaches at the end, 89 return True, if opera,on reaches 1 at the end return False.
"""

def one_or_eight(no):
    list1 = []
    temp = no
    while no < 89:
        if ((no//10)== 0):
            no = no**2
        else:
            while temp > 0:
                digit = temp % 10
                no += digit ** 2
                temp //= 10
    if no == 1:
        return False
    if no == 89:
        return True


no = int(input())
output = one_or_eight(no)
print(output)