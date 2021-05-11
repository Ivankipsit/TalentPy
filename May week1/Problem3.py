"""
Create a function to compute sum of digits. Call this sum of digits function
to find the sum of digits of numbers ranges from 1001 to 22000.
"""


def sum_Dig(num):
    sum = 0
    temp = num
    if (1000 < num < 22001):
        while temp > 0:
            digit = temp % 10
            sum += digit 
            temp //= 10
        return sum
    else:
        return "Enter number between 1000 and 22001"
num = int(input())
print(sum_Dig(num))