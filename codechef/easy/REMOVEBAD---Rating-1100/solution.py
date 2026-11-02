# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    ints=list(map(int,input().split()))
    act_ints=set(ints)
    maxi=max(ints.count(x) for x in act_ints)
    ops=N-maxi
    print(ops)