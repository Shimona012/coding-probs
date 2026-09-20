# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    p1,p2=0,0
    for k in range(N):
        n1,n2=[sum(map(int,x))for x in input().split()]
        if n1==n2:
            p1+=1
            p2+=1
        elif n1>n2:
            p1+=1
        else:
            p2+=1
    if p1>p2:
        print(0,p1)
    elif p2>p1:
        print(1,p2)
    else: 
        print(2,p1)