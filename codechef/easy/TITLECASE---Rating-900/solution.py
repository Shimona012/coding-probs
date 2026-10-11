# cook your dish here
T=int(input())
for i in range(T):
    S=input()
    words=S.split()
    for j in range(len(words)):
        if words[j].isupper():
            words[j]=words[j]
        else:
            words[j]=words[j].capitalize()
    print(" ".join(words))
