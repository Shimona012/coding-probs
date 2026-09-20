# cook your dish here
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    list_ints=sorted(list(map(int,input().split())))
    if N==1:
        print("YES")
    else:
        if list_ints[0]+list_ints[-1]<=K:
            print("YES")
        else:
            print("NO")
        