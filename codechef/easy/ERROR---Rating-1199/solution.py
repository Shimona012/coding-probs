# cook your dish here
T=int(input())
for i in range(T):
    s=input()
    if '010' in s or '101' in s:
        print("Good")
    else:
        print("Bad")
