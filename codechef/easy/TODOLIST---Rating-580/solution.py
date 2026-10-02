# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    Difficult=list(map(int,input().split()))
    remov=sum(1 for i in Difficult if i>=1000)
    print(remov)