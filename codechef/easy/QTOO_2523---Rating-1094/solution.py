# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    strings=list(map(int,input().split()))
    skip=0
    for j in range(1,N):
        skip+=(abs(strings[j]-strings[j-1])-1)
    print(skip)