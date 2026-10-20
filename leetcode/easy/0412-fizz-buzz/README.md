# Fizz Buzz

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `n`, return  *a string array* `answer` *(**1-indexed**) where* :

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.

 

 **Example 1:** 

```
Input: n = 3
Output: ["1","2","Fizz"]

```

 **Example 2:** 

```
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

```

 **Example 3:** 

```
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

```

 

 **Constraints:** 

- 1 <= n <= 104

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.6 MB (beats 53.54%)  
**Submitted:** 2026-10-20T12:50:35.103Z  

```py
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        arr=list()
        for i in range(1,n+1):
            if i%3==0:
                if i%5==0:
                    arr.append("FizzBuzz")
                    continue
                else:
                    arr.append("Fizz")
                    continue
            elif i%5==0:
                if i%3==0:
                    arr.append("FizzBuzz")
                    continue
                else:
                    arr.append("Buzz")
                    continue
            else:
                arr.append(str(i))
                continue
        return arr

                
```

---

[View on LeetCode](https://leetcode.com/problems/fizz-buzz/)