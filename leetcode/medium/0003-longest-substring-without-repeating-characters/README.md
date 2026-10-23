# Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, find the length of the  **longest**   **substring**  without duplicate characters.

 

 **Example 1:** 

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

 **Example 2:** 

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

 **Example 3:** 

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

 **Constraints:** 

- 0 <= s.length <= 105
- s consists of English letters, digits, symbols and spaces.

## Solution

**Language:** Python  
**Runtime:** 231 ms (beats 34.05%)  
**Memory:** 21.1 MB (beats 12.84%)  
**Submitted:** 2026-10-23T18:21:37.868Z  

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        poss,taken,inuse=set(),set(),str()
        for i in s:
            if i in taken:
                poss.add(inuse)
                while i in taken:
                    taken.remove(inuse[0])
                    inuse=inuse[1:]
            taken.add(i)
            inuse+=i
        return max(len(inuse),max(map(len,poss),default=0))
```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)