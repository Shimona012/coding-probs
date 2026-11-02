# QTOO_2523 - Rating 1094

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-02T17:07:01.388Z  

```py
# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    strings=list(map(int,input().split()))
    skip=0
    for j in range(1,N):
        skip+=(abs(strings[j]-strings[j-1])-1)
    print(skip)
```

---

[View on CodeChef](https://www.codechef.com/problems/QTOO_2523)