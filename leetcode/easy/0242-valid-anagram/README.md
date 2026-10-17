# Valid Anagram

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

 **Example 1:** 

 **Input:**  s = "anagram", t = "nagaram"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "rat", t = "car"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

 

 **Follow up:**  What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 98.73%)  
**Memory:** 12.7 MB (beats 47.10%)  
**Submitted:** 2026-10-17T09:11:18.751Z  

```py
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_s=set(list(s))
        letter_t=set(list(t))
        if len(letter_t)!=len(letter_s):
            return False
        else:
            for i in list(letter_s):
                if t.count(i)!=s.count(i):
                    return False
            else:
                return True


        
```

---

[View on LeetCode](https://leetcode.com/problems/valid-anagram/)