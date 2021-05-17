"""
Sam College of Cartoon
You have to create different functions for Sam’s college of cartoon. Please find the functions list
below -
--Function 1:
• Give me a random cartoon character:
• This function should take N arguments, where N is not fixed and ranges from 0 to
many. This function should return a random character from the N argument.
• For example: If arguments are “Dora”, “Shin Chan”, “Poke mon” etc… this function
should return any one of the above character. (Eg: “Dora”) and must be random.
• If the argument length for the function is 0, then this function should return False
(boolean) as output.

--Function 2:
• Swap the cartoon character: - Function 2
• This function should call function 1 (above) and if function 1 returns False, then this
function should also return False.
• Else, get the character and swap the letters of characters. (Upper case to lower case
and vice versa)
• For example: if the function gives you “Dora”, then output should be “dORA”.
• Return the swapped output as result.

--Function 3:
• Muliply the swap: - Func?on 3
• This function should take 2 arguments. First one is cartoon_character and second one as
multiplier. If the user is not specifying multiplier value it should take 3. Else if user
specified any value, take that value into account.
• Multiply the cartoon_character (first argument) with the multiplier value given.
• Example: If cartoon_character is “Dora”, multiplier is 5, then DoraDoraDoraDoraDora
should be the output.

--Function 4:
• Main function:
• Create a function with name main()
• Call function 2, if it is not returning False, pass the output of function 2 as a first
parameter to function 3 and get the output from F3 and print it.
• If call to function 2, gives False, print the message “Oops! No cartoon selected”.
"""


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
        return "Oops! No cartoon Selected." 
    else:
        return Function3((Function2((Function1(list1)))),M) 
list1 = input().split(",")
M = input()
if M == "":
    print(main(list1))
else:
    M = int(M)
    print(main(list1,M))