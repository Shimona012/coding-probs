# cook your dish here
n=input()
d=len(n)

num=str(int(n) ** 2)

p1=int(num[:d])
try:
    p2=int(num[d:])
except ValueError:
    p2=0
if d>1:
    p3=int(num[:d-1])
else:
    p3=0
try:
    p4=int(num[d-1:])
except:
    p4=0

if p1+p2==int(n) or p3+p4==int(n):
    print("yes")
else:
    print("no")