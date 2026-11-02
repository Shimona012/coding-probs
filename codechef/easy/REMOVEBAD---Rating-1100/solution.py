# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    ints=list(map(int,input().split()))
    act_ints=set(ints)
    nums=dict()
    maxi=0
    for j in act_ints:
        nums[j]=ints.count(j)
        if ints.count(j)>maxi:
            maxi=ints.count(j)
    ops=N-maxi
    print(ops)