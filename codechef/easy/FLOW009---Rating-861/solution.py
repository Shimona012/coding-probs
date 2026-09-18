# cook your dish here
T=int(input())
for i in range(T):
    info=input().split()
    quant=int(info[0])
    price=float(info[1])
    if quant>1000:
        amt=0.9*(quant*price)
    else:
        amt=quant*price
    print(amt)