# cook your dish here
S=input().lower()
freq=dict()
for i in S:
    if i.isalpha():
        freq[i]=freq.get(i,0)+1
print(max(freq.keys(),key=freq.get))