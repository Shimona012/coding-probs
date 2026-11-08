T=int(input())
for i in range(T):
    N=int(input())
    nums=list(map(int,input().strip().split()))
    dis_num=set(nums)
    if len(dis_num)==2*N:
        print("Yes")
    else:
        for j in dis_num:
            if nums.count(j)>2:
                print("No")
                break
        else:
            print("Yes")