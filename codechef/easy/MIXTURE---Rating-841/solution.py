# cook your dish here
T=int(input())
for i in range(T):
    A,B=input().split()
    if int(A)>0 and int(B)>0:
        print("Solution")
    elif int(A)==0:
        print("Liquid")
    else:
        print("Solid")
