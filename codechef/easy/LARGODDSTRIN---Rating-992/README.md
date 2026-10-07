# LARGODDSTRIN - Rating 992

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T12:28:19.498Z  

```py
t = int(input())

while t > 0:
    s = input().strip()
    dates=s.split("/")
    if int(dates[0])<32 and int(dates[1])<13:
        if int(dates[0])<13 and int(dates[1])<32:
            print("BOTH")
        else:
            print("DD/MM/YYYY")
    else:
        print("MM/DD/YYYY")
        
    t -= 1

```

---

[View on CodeChef](https://www.codechef.com/problems/LARGODDSTRIN)