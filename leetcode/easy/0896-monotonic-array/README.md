# Monotonic Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

An array is  **monotonic**  if it is either monotone increasing or monotone decreasing.

An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array `nums`, return `true` *if the given array is monotonic, or* `false` *otherwise*.

 

 **Example 1:** 

```
Input: nums = [1,2,2,3]
Output: true

```

 **Example 2:** 

```
Input: nums = [6,5,4,4]
Output: true

```

 **Example 3:** 

```
Input: nums = [1,3,2]
Output: false

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -105 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 80 ms (beats 25.06%)  
**Memory:** 21.2 MB (beats 5.83%)  
**Submitted:** 2026-10-17T11:34:03.236Z  

```py
class Solution(object):
    def isMonotonic(self, nums):
        """:type nums: List[int]:rtype: bool"""
        sorted_nums=sorted(nums)
        if sorted_nums==nums or sorted_nums[::-1]==nums:
            return True
        else:
            return False
```

---

[View on LeetCode](https://leetcode.com/problems/monotonic-array/)