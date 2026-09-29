# cook your dish here
T=int(input())
for i in range(T):
    X,A,B=map(int,input().split())
    total=A+B*2
    if total<X:
        print("NotQualify")
    else:
        print("Qualify")
