# cook your dish here
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    if X>=Y:
        print("PIZZA")
    elif X<Z:
        print("NOTHING")
    else:
        print("BURGER")