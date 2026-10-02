# cook your dish here
from math import *
T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    candies=N-X
    if candies<1:
        print(0)
    else:
        print(ceil(candies/4))
