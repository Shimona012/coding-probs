# Multiply Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

 **Note:**  You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

 **Example 1:** 

```
Input: num1 = "2", num2 = "3"
Output: "6"

```

 **Example 2:** 

```
Input: num1 = "123", num2 = "456"
Output: "56088"

```

 

 **Constraints:** 

- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only.
- Both num1 and num2 do not contain any leading zero, except the number 0 itself.

## Solution

**Language:** Python  
**Runtime:** 40 ms (beats 55.54%)  
**Memory:** 19.4 MB (beats 41.74%)  
**Submitted:** 2026-10-19T07:45:55.375Z  

```py
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        
        m,n= len(num1),len(num2)
        res=[0]*(m + n)
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                prod=int(num1[i])*int(num2[j])
                p1,p2=i+j,i+j+1
                prod+=res[p2]
                res[p1]+=prod//10
                res[p2]=prod%10
        result_str="".join(map(str,res)).lstrip("0")
        return result_str if result_str else "0"
```

---

[View on LeetCode](https://leetcode.com/problems/multiply-strings/)