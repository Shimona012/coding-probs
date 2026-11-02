# REMOVEBAD - Rating 1100

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Remove Bad elements

Chef has an array $A$ of length $N$.

In one operation, Chef can remove  **any one**  element from the array.

Determine the  **minimum**  number of operations required to make all the elements  **same**.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of each test case contains a single integer $N$ —the length of Array $A$. Next line contains $N$ space-separated integers $A_1, A_2, A_3, \dots, A_N$ - denoting the array $A$.
### Output Format

For each test case, output the  **minimum**  number of operations required to make all the elements same.

### Constraints
- $1 \leq T \leq 4000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq N$
- Sum of $N$ over all test cases do not exceed $3 \cdot 10^5$
### Sample 1:
Input
Output

```
4
3
3 3 3
6
1 3 2 1 2 2
4
1 2 1 2
5
1 3 2 4 5

```

```
0
3
2
4

```

### Explanation:

 **Test case $1$:**  All the elements are already same. Thus we need to perform zero operations.

 **Test case $2$:**  We remove the elements $A_1, A_2,$ and $A_4$ using three operations. The array becomes $[2, 2, 2]$ where all elements are same.

 **Test case $3$:**  We remove the elements $A_1$ and $A_3$ using two operations. The array becomes $[2, 2]$ where all elements are same.

 **Test case $4$:**  We remove the elements $A_1, A_2, A_3,$ and $A_4$ using four operations. The array becomes $[5]$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-02T17:12:55.399Z  

```py
# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    ints=list(map(int,input().split()))
    act_ints=set(ints)
    nums=dict()
    maxi=0
    for j in act_ints:
        nums[j]=ints.count(j)
        if ints.count(j)>maxi:
            maxi=ints.count(j)
    ops=N-maxi
    print(ops)
```

---

[View on CodeChef](https://www.codechef.com/problems/REMOVEBAD)