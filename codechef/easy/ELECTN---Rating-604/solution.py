# cook your dish here
T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    voters=list(map(int,input().split()))
    count=len(voters)
    count-=sum(1 for j in voters if j < X)
    print(count)