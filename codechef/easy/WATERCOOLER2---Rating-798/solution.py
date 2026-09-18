# cook your dish here
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    x=int(X)
    month=0
    while X<Y:
        month+=1
        X+=x
    print(month)
