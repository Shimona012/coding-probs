# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    digitsum=sum(list(map(int,list(str(N)))))
    X=N+1
    if digitsum%2==0:
        if sum(list(map(int,list(str(X)))))%2==0:
            X+=1
    else:
        if sum(list(map(int,list(str(X)))))%2!=0:
            X+=1
    print(X)
        
    
