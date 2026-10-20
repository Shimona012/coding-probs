# Longest Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` which consists of lowercase or uppercase letters, return the length of the  **longest palindrome**  that can be built with those letters.

Letters are  **case sensitive**, for example, `"Aa"` is not considered a palindrome.

 

 **Example 1:** 

```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

```

 **Example 2:** 

```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

```

 

 **Constraints:** 

- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 62.39%)  
**Memory:** 19 MB (beats 98.24%)  
**Submitted:** 2026-10-20T12:55:35.441Z  

```py
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=dict()
        length=0
        for i in s:
            count[i] = count.get(i, 0) + 1
        for f in count.values():
            length+=(f//2) * 2
        if length<len(s):
            length+= 1
        return length
                
            
```

---

[View on LeetCode](https://leetcode.com/problems/longest-palindrome/)