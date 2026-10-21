# Find the K-th Character in String Game I

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a  **positive**  integer `k`.

Now Bob will ask Alice to perform the following operation  **forever** :

- Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.

For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the `kth` character in `word`, after enough operations have been done for `word` to have  **at least**  `k` characters.

 

 **Example 1:** 

 **Input:**  k = 5

 **Output:**  "b"

 **Explanation:** 

Initially, `word = "a"`. We need to do the operation three times:

- Generated string is "b", word becomes "ab".
- Generated string is "bc", word becomes "abbc".
- Generated string is "bccd", word becomes "abbcbccd".

 **Example 2:** 

 **Input:**  k = 10

 **Output:**  "c"

 

 **Constraints:** 

- 1 <= k <= 500

## Solution

**Language:** Python  
**Runtime:** 13 ms (beats 26.87%)  
**Memory:** 19.1 MB (beats 96.59%)  
**Submitted:** 2026-10-21T18:09:05.327Z  

```py
class Solution:
    def kthCharacter(self, k: int) -> str:
        word='a'
        start=1
        while len(word)<=k:
            word += ''.join(chr((ord(c) - 96) % 26 + 97) for c in word[:start])
            start *= 2
        return word[k - 1]
```

---

[View on LeetCode](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/)