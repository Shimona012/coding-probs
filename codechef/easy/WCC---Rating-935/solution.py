# cook your dish here
T=int(input())
for i in range(T):
    X=int(input())
    result=input()
    results=list()
    results.extend((result.count('C')*2,result.count('N')*2,result.count('D')))
    if results[0]>results[1]:
        print(60*X)
    elif results[0]==results[1]:
        print(55*X)
    else:
        print(40*X)
