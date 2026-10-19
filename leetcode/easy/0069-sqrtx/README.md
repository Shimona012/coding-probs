# Sqrt(x)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a non-negative integer `x`, return  *the square root of* `x` *rounded down to the nearest integer*. The returned integer should be  **non-negative**  as well.

You  **must not use**  any built-in exponent function or operator.

- For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

 **Example 1:** 

```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

```

 **Example 2:** 

```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

```

 

 **Constraints:** 

- 0 <= x <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 1239 ms (beats 10.63%)  
**Memory:** 19.3 MB (beats 19.35%)  
**Submitted:** 2026-10-19T08:46:12.275Z  

```py
class Solution:
    def mySqrt(self, x: int) -> int:
        n=x//2
        num=0
        if x<2:
            return x
        for i in range(n + 1):
            if i*i<=x:
                num=i
            else:
                break

        return num
        
```

---

[View on LeetCode](https://leetcode.com/problems/sqrtx/)