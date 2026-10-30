import sys
def is_prime(x):
    if x<=1:
        return False
    if x<=3:
        return True
    if x%2==0 or x%3==0:
        return False
    j=5
    while j*j<=x:
        if x%j==0 or x%(j+2)==0:
            return False
        j+=6
    return True
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    for x in range(m,n+1):
        if is_prime(x):
            print(x)
    print()