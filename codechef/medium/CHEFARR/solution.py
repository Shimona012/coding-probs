# cook your dish here
N=int(input())
A=list(map(int,input().split()))
count=0
ways=0
tot_sum=sum(A)
if tot_sum%3==0:
    small_sol=tot_sum//3
    big_sol=small_sol*2
    temp_sum=0
    for i in range(N-1):
        temp_sum+=A[i]
        if temp_sum==big_sol:
            ways+=count
        if temp_sum==small_sol:
            count+=1
        
    print(ways)
else:
    print(0)
