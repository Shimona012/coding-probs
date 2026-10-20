# Convert a Number to Hexadecimal

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a 32-bit integer `num`, return  *a string representing its hexadecimal representation*. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

 **Note:** You are not allowed to use any built-in library method to directly solve this problem.

 

 **Example 1:** 

```
Input: num = 26
Output: "1a"

```

 **Example 2:** 

```
Input: num = -1
Output: "ffffffff"

```

 

 **Constraints:** 

- -231 <= num <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.1 MB (beats 89.23%)  
**Submitted:** 2026-10-20T13:54:13.183Z  

```py
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        digits="0123456789abcdef"
        num&=0xFFFFFFFF
        hex_code=str()
        while num:
            hex_code+=digits[num % 16]
            num //= 16
        return hex_code[::-1]
            
```

---

[View on LeetCode](https://leetcode.com/problems/convert-a-number-to-hexadecimal/)