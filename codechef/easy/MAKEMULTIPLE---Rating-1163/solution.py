# cook your dish here
T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    if A==B or B>=2*A: 
        print("YES")
    else:
        print("NO")
 