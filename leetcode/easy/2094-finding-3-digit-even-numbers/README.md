# Finding 3-Digit Even Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `digits`, where each element is a digit. The array may contain duplicates.

You need to find  **all**  the  **unique**  integers that follow the given requirements:

- The integer consists of the concatenation of three elements from digits in any arbitrary order.
- The integer does not have leading zeros.
- The integer is even.

For example, if the given `digits` were `[1, 2, 3]`, integers `132` and `312` follow the requirements.

Return  *a  **sorted**  array of the unique integers.* 

 

 **Example 1:** 

```
Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array. 
Notice that there are no odd integers or integers with leading zeros.

```

 **Example 2:** 

```
Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 

```

 **Example 3:** 

```
Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.

```

 

 **Constraints:** 

- 3 <= digits.length <= 100
- 0 <= digits[i] <= 9

## Solution

**Language:** Python  
**Runtime:** 2693 ms (beats 30.05%)  
**Memory:** 19.2 MB (beats 82.04%)  
**Submitted:** 2026-10-21T18:12:15.743Z  

```py
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        nums=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i!=j and j!=k and i!=k and digits[i]!=0 and digits[k]%2 == 0:
                        nums.add(digits[i]*100 + digits[j] * 10 + digits[k])
        return sorted(nums) 
```

---

[View on LeetCode](https://leetcode.com/problems/finding-3-digit-even-numbers/)