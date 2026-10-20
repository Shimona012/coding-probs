# Ransom Note

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `ransomNote` and `magazine`, return `true` *if* `ransomNote` *can be constructed by using the letters from* `magazine` *and* `false` *otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

 

 **Example 1:** 

```
Input: ransomNote = "a", magazine = "b"
Output: false

```

 **Example 2:** 

```
Input: ransomNote = "aa", magazine = "ab"
Output: false

```

 **Example 3:** 

```
Input: ransomNote = "aa", magazine = "aab"
Output: true

```

 

 **Constraints:** 

- 1 <= ransomNote.length, magazine.length <= 105
- ransomNote and magazine consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 27 ms (beats 31.89%)  
**Memory:** 19.4 MB (beats 92.30%)  
**Submitted:** 2026-10-20T14:27:46.317Z  

```py
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        d = {}
        for i in magazine:
            d[i]=d.get(i, 0) + 1
        for i in ransomNote:
            if i not in d or d[i]==0:
                return False
            d[i]-=1
        return True
        n

            
```

---

[View on LeetCode](https://leetcode.com/problems/ransom-note/)