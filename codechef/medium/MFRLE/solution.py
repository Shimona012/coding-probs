# cook your dish here
S=input().lower()
freq=dict()
for i in S:
    if i.isalpha():
        freq[i]=freq.get(i,0)+1
m=max(freq.values())
print(sorted([i for i in freq if freq[i]==m])[0])