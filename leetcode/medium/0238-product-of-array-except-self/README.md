# Product of Array Except Self

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, return  *an array*  `answer`  *such that*  `answer[i]`  *is equal to the product of all the elements of*  `nums`  *except*  `nums[i]`.

The product of any prefix or suffix of `nums` is  **guaranteed**  to fit in a  **32-bit**  integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

 

 **Example 1:** 

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

```

 **Example 2:** 

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

```

 

 **Constraints:** 

- 2 <= nums.length <= 105
- -30 <= nums[i] <= 30
- The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

 

 **Follow up:**  Can you solve the problem in `O(1)` extra space complexity? (The output array  **does not**  count as extra space for space complexity analysis.)

## Solution

**Language:** Python  
**Runtime:** 31 ms (beats 60.71%)  
**Memory:** 20.1 MB (beats 73.79%)  
**Submitted:** 2026-09-30T16:34:37.255Z  

```py
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #answer=[]
        answer=[1]*len(nums)
        #prefix=[1]
        #suffix=[1]*len(nums)
        for i in range(1,len(nums)):
            #prod=prefix[i-1]*nums[i-1]
            #prefix.append(prod)
            answer[i]=answer[i-1]*nums[i-1]
        #for j in range(len(nums)-2,-1,-1):
        #    suffix[j]=suffix[j+1]*nums[j+1]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]
        #for k in range(len(nums)):
        #    answer.append(prefix[k]*suffix[k])
        return answer
```

---

[View on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)