# Repeated Substring Pattern

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

 **Example 1:** 

```
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

```

 **Example 2:** 

```
Input: s = "aba"
Output: false

```

 **Example 3:** 

```
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

```

 

 **Constraints:** 

- 1 <= s.length <= 104
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 73.50%)  
**Memory:** 12.1 MB (beats 100.00%)  
**Submitted:** 2026-10-17T09:21:04.378Z  

```py
class Solution(object):
    def repeatedSubstringPattern(self, s):
        #:type s: str:rtype: bool
        return s in (s + s)[1:-1]
```

---

[View on LeetCode](https://leetcode.com/problems/repeated-substring-pattern/)