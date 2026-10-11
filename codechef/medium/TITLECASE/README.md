# TITLECASE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T17:04:54.828Z  

```py
def findLargestOddSubstring(num):
    count=''
    max_count=''
    for i in range(len(num)):
        if int(num[i])%2!=0:
            max_count=num[:i+1]
    if max_count=='':
        return -1
    else:
        return max_count
    

```

---

[View on CodeChef](https://www.codechef.com/problems/TITLECASE)