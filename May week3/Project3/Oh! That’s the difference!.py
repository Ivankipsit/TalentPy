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