# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    info=sorted(list(map(int,input().split())),reverse=True)
    pair=0
    for j in range(N):
        for k in range(j+1,N):
            pair = max(pair, sum(map(int, str(info[j] * info[k]))))

    print(pair)    