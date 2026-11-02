# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    ints=list(map(int,input().split()))
    nums=dict()
    for j in ints:
        nums[j] = nums.get(j, 0) + 1
    maxi=max(nums.values())
    ops=N-maxi
    print(ops)