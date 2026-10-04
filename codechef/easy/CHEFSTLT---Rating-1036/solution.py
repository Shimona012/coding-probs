# cook your dish here
T=int(input())
for i in range(T):
    S1=input()
    S2=input()
    min_diff=0
    max_diff=0
    for j in range(len(S1)):
        if S1[j]=='?' or S2[j]=='?':
            max_diff+=1
        elif S1[j]!=S2[j]:
            min_diff+=1
            max_diff+=1

    print(min_diff,max_diff)