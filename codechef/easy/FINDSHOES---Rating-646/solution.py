# cook your dish here
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    if N>M:
        print(N+N-M)
    else:
        print(N)