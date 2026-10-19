# Check If It Is a Straight Line

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `coordinates`, `coordinates[i] = [x, y]`, where `[x, y]` represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

 **Example 1:** 

```
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

```

 **Example 2:** 

```
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

```

 

 **Constraints:** 

- 2 <= coordinates.length <= 1000
- coordinates[i].length == 2
- -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
- coordinates contains no duplicate point.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.5 MB (beats 82.36%)  
**Submitted:** 2026-10-19T07:53:53.885Z  

```py
class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x=coordinates[1][0]-coordinates[0][0]
        y=coordinates[1][1]-coordinates[0][1]
        for i in coordinates[2:]:
            if (i[0]-coordinates[0][0])*y!=(i[1]-coordinates[0][1])*x:
                return False
        return True
```

---

[View on LeetCode](https://leetcode.com/problems/check-if-it-is-a-straight-line/)