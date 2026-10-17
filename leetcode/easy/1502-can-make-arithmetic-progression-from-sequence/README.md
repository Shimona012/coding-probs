# Can Make Arithmetic Progression From Sequence

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A sequence of numbers is called an  **arithmetic progression**  if the difference between any two consecutive elements is the same.

Given an array of numbers `arr`, return `true`  *if the array can be rearranged to form an  **arithmetic progression**. Otherwise, return*  `false`.

 

 **Example 1:** 

```
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

```

 **Example 2:** 

```
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

```

 

 **Constraints:** 

- 2 <= arr.length <= 1000
- -106 <= arr[i] <= 106

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 41.07%)  
**Memory:** 12.4 MB (beats 81.30%)  
**Submitted:** 2026-10-17T11:21:46.589Z  

```py
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """:type arr: List[int]:rtype: bool"""
        arr.sort()
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != arr[1] - arr[0]:
                return False
        return True 
```

---

[View on LeetCode](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/)