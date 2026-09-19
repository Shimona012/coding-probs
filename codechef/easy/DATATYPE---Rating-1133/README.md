# DATATYPE - Rating 1133

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T13:41:23.171Z  

```py
# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    info=sorted(list(map(int,input().split())),reverse=True)
    pair=0
    for j in range(N):
        for k in range(j+1,N):
            pair = max(pair, sum(map(int, str(info[j] * info[k]))))

    print(pair)    
```

---

[View on CodeChef](https://www.codechef.com/problems/DATATYPE)