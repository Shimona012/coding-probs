# cook your dish here
N=int(input())
W=0
L=0
cum_p1=0
cum_p2=0
for i in range(N):
    p1,p2=map(int,input().split())
    cum_p1+=p1
    cum_p2+=p2
    if abs(cum_p1-cum_p2)>L:
        if cum_p2>cum_p1:
            W=2
        else:
            W=1
        L=abs(cum_p1-cum_p2)
print(W,L)
    