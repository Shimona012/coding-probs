# cook your dish here
T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    z=1
    while True:
        if z%2==1:
            A-=z
            if A<0:
                print("Bob")
                break
        else:
            B-=z
            if B<0:
                print("Limak")
                break
        z+=1