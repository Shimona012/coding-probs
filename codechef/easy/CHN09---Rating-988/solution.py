# cook your dish here
T=int(input())
for i in range(T):
    s=input()
    a=s.count('a')
    b=s.count('b')
    if a>b:
        print(b)
    else:
        print(a)