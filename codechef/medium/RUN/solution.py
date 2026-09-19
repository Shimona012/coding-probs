T=input()
for i in range(int(T)):
    N=int(input())
    info=list(map(int,input().split()))
    M=float(input())
    total = sum(info)
    M%=total
    if M==0:
        M=total
    sumD=0
    for i in range(N):
        sumD+=info[i]
        if sumD>=M:
            print(i+1)
            break
        