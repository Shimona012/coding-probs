# EXAMTIME - Rating 1001

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-31T12:08:00.934Z  

```py
# cook your dish here
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    withdraw=list(map(int,input().split()))
    output=list([0]*N)
    for j in range(N):
        if K>=withdraw[j]:
            output[j]=1
            K-=withdraw[j]
    print(''.join(map(str,output)))
```

---

[View on CodeChef](https://www.codechef.com/problems/EXAMTIME)