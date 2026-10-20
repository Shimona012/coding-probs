# First Unique Character in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, find the  **first**  non-repeating character in it and return its index. If it  **does not**  exist, return `-1`.

 

 **Example 1:** 

 **Input:**  s = "leetcode"

 **Output:**  0

 **Explanation:** 

The character `'l'` at index 0 is the first character that does not occur at any other index.

 **Example 2:** 

 **Input:**  s = "loveleetcode"

 **Output:**  2

 **Example 3:** 

 **Input:**  s = "aabb"

 **Output:**  -1

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 67 ms (beats 67.81%)  
**Memory:** 19.6 MB (beats 57.60%)  
**Submitted:** 2026-10-20T14:12:40.950Z  

```py
from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        od=OrderedDict()
        for i,ch in enumerate(s):
            if ch not in od:
                od[ch]=[1,i]
            else:
                od[ch][0]+=1
        for ch,(count,index) in od.items():
            if count==1:
                return index
        return -1
```

---

[View on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)