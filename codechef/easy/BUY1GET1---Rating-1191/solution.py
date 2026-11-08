# cook your dish here
T=int(input())
for i in range(T):
    S=input().strip()
    jewels=set(list(S))
    money=0
    for j in jewels:
        num=S.count(j)
        money+=num//2+num%2
    print(money)