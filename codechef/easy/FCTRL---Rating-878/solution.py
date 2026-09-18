# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    start=5
    count=0
    while start<=N:
        count+=N//start
        start*=5
    print(count)