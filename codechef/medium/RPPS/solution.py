# cook your dish here
s=input()
char_count=dict()
for i in range(len(s)-1):
    string=s[i]+s[i+1]
    existing_count=char_count.setdefault(string,0)
    new_count=existing_count+1
    char_count[string]=new_count
multi=0
for k,v in char_count.items():
    if v>1:
        multi+=1
print(multi)