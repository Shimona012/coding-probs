# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    subs=dict()
    tot=0
    for j in range(N):
        p,s=map(int,input().split())
        if p in subs:
            pts=subs[p]
            pts.append(s)
            subs[p]=pts
        else:
            subs[p]=[s]
        
    for k in subs:
        if k<9:
            tot+=max(subs[k])
    print(tot)