# Add Binary

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two binary strings `a` and `b`, return  *their sum as a binary string*.

 

 **Example 1:** 

```
Input: a = "11", b = "1"
Output: "100"

```

 **Example 2:** 

```
Input: a = "1010", b = "1011"
Output: "10101"

```

 

 **Constraints:** 

- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 51.22%)  
**Submitted:** 2026-10-18T17:35:14.501Z  

```py
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=int(a,2),int(b,2)
        sum_b=str(bin(a+b))
        return sum_b[2:]
        
```

---

[View on LeetCode](https://leetcode.com/problems/add-binary/)