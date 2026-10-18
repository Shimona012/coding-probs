# Find Winner on a Tic Tac Toe Game

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

**Tic-tac-toe**  is played by two players `A` and `B` on a `3 x 3` grid. The rules of Tic-Tac-Toe are:

- Players take turns placing characters into empty squares ' '.
- The first player A always places 'X' characters, while the second player B always places 'O' characters.
- 'X' and 'O' characters are always placed into empty squares, never on filled ones.
- The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
- The game also ends if all squares are non-empty.
- No more moves can be played if the game is over.

Given a 2D integer array `moves` where `moves[i] = [rowi, coli]` indicates that the `ith` move will be played on `grid[rowi][coli]`. return  *the winner of the game if it exists*  (`A` or `B`). In case the game ends in a draw return `"Draw"`. If there are still movements to play return `"Pending"`.

You can assume that `moves` is valid (i.e., it follows the rules of  **Tic-Tac-Toe**), the grid is initially empty, and `A` will play first.

 

 **Example 1:** 

```
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

```

 **Example 2:** 

```
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

```

 **Example 3:** 

```
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.

```

 

 **Constraints:** 

- 1 <= moves.length <= 9
- moves[i].length == 2
- 0 <= rowi, coli <= 2
- There are no repeated elements on moves.
- moves follow the rules of tic tac toe.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.3 MB (beats 89.53%)  
**Submitted:** 2026-10-18T15:13:56.849Z  

```py
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        A=moves[::2]
        B=moves[1::2]
        wins=[
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)]
        ]

        for win in wins:
            if all(list(cell) in A for cell in win):
                return 'A'
            if all(list(cell) in B for cell in win):
                return 'B'

        if len(moves) == 9:
            return 'Draw'

        return 'Pending'

```

---

[View on LeetCode](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)