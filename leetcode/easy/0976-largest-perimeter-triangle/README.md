# Largest Perimeter Triangle

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, return  *the largest perimeter of a triangle with a non-zero area, formed from three of these lengths*. If it is impossible to form any triangle of a non-zero area, return `0`.

 

 **Example 1:** 

```
Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

```

 **Example 2:** 

```
Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

```

 

 **Constraints:** 

- 3 <= nums.length <= 104
- 1 <= nums[i] <= 106

## Solution

**Language:** Python  
**Runtime:** 17 ms (beats 34.52%)  
**Memory:** 20.2 MB (beats 99.73%)  
**Submitted:** 2026-10-18T17:22:39.559Z  

```py
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            sides=nums[i:i+3]
            if sides[0]<sides[1]+sides[2]:
                return sum(sides)
        return 0
```

---

[View on LeetCode](https://leetcode.com/problems/largest-perimeter-triangle/)