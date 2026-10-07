# cook your dish here
S=input().lower()
only_chars=str()
freq=dict()
for i in S:
    if i.isalpha()==True:
        only_chars+=i
for j in only_chars:
    freq.setdefault(j,only_chars.count(j))
print(max(freq.keys(),key=freq.get))