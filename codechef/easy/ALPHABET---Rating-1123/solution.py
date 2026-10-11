# cook your dish here
S=input()
N=int(input())
for i in range(N):
    W=input()
    if all(letter in S for letter in W):
        print("Yes")
    else:
        print("No")