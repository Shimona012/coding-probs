# Permutations

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in  **any order**.

 

 **Example 1:** 

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```

 **Example 2:** 

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]

```

 **Example 3:** 

```
Input: nums = [1]
Output: [[1]]

```

 

 **Constraints:** 

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.

## Solution

**Language:** Python  
**Runtime:** 22 ms (beats 1.84%)  
**Memory:** 19.3 MB (beats 95.38%)  
**Submitted:** 2026-10-27T14:05:26.436Z  

```py
import random
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms=set()
        pnr=1
        for i in range(1,len(nums)+1):
            pnr*=i    
        while len(perms)!=pnr:
                p=tuple(random.sample(nums,len(nums)))
                perms.add(p)
        return [list(p) for p in perms]
```

---

[View on LeetCode](https://leetcode.com/problems/permutations/)