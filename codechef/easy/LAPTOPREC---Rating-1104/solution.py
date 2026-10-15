# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    recs=list(map(int,input().split()))
    max_recs=sorted(set(recs),key=lambda x:recs.count(x),reverse=True)
    if len(max_recs)>1 and recs.count(max_recs[0])==recs.count(max_recs[1]):
        print("CONFUSED")
    else:
        print(max_recs[0])