# cook your dish here
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    month=0
    while X<Y:
        month+=1
        X+=X
    print(month)
