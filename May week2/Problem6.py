"""
String Calculator - Implement String calculator with following functions.
• Function that reverses the given string S. (A)
• Function that returns total A’s available (it can be ‘a’ or ‘A’) int given
string S. (B)
• Function that takes 2 inputs string S and index and returns element at
given index. If the index is not available, it should return 0 as the
output. (C)
• Function that multiples given string 5 times (D)
- Implement all the above functions.
- Get input and pass it to the reverse function, get the output from it and call
function C, function C takes 2 params, first param should be output from function
A and second param should be output from function B. Get the output. If the
output is not 0, call function D and print output. Else call print “Completed without
multiply” as the output.
Sample I/O:
Input: “Hari”
Output:
- Reverse of Hari => iraH
- Output from function C => C(“iraH”, 1) => r
- Final output = 5 times of r = rrrrr.
"""

def A(string):
    return string[::-1]
    
def B(string):
    count = 0
    list1 = []
    list1 = list(string)
    for ele in list1:
        if ele in ["a", "A"]:
            count += 1
    return count

def C(string,index):
    return string[index]
    
def D(string,index):
    if index == 0:
        return "Complete without multiply"
    else:
        return string*5
    
string = input()
print(D(C(A(string),(B(A(string)))),(B(A(string)))))