# cook your dish here
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    withdraw=list(map(int,input().split()))
    output=list([0]*N)
    for j in range(N):
        if K>=withdraw[j]:
            output[j]=1
            K-=withdraw[j]
    print(''.join(map(str,output)))