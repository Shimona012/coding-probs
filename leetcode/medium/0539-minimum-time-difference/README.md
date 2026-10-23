# Minimum Time Difference

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a list of 24-hour clock time points in  **"HH:MM"**  format, return  *the minimum  **minutes**  difference between any two time-points in the list*.

 

 **Example 1:** 

```
Input: timePoints = ["23:59","00:00"]
Output: 1

```

 **Example 2:** 

```
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

```

 

 **Constraints:** 

- 2 <= timePoints.length <= 2 * 104
- timePoints[i] is in the format "HH:MM".

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 77.31%)  
**Memory:** 21.4 MB (beats 15.01%)  
**Submitted:** 2026-10-23T18:11:53.342Z  

```py
class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        diff=list()
        for t in timePoints:
            h=int(t[0:2])
            m=int(t[3:])
            diff.append(h*60+m)
        diff.sort()
        ans=1440-diff[-1]+diff[0]
        for i in range(1,len(diff)):
            ans=min(ans,diff[i]-diff[i-1])
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-time-difference/)