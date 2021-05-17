"""
Create a function difference which takes a string S and character K. Find the difference between
first occurrence of K and last occurrence of K in string S. Convert the input to lower case before
processing.
Check for following conditions :
1. If K not occurred in S, return “K not found in S”.
2. If K occurred only once in S, return “Difference can’t be calculated”.
3. If K occurs more than once, return count of difference.
"""


def diff(S,K):
    list1 = list(S)
    list2 = []
    for i in range(len(S)):
        if S[i] == K:
#            print(i,S[i])
            k = int(i)
            list2.append(k)
    mini = list2[0]
    maxi = list2[-1]
    a = (maxi-mini)-1
    return a
S = str(input().lower())
K = str(input().lower())
print(diff(S,K))