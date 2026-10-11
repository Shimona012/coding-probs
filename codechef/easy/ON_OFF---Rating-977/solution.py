t = int(input())

while t > 0:
    n = int(input())
    s = input()
    r = input()
    count=0
    for i in range(n):
        if s[i]!=r[i]:
            count+=1
    if count%2==0:
        print(1)
    else:
        print(0)
    t -= 1
