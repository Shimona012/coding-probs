# MAKEMULTIPLE - Rating 1163

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Make Multiple

Chef has two integers $A$ and $B$ $(A \leq B)$.

Chef can choose any  **non-negative**  integer $X$ and add them to both $A$ and $B$. Find whether it is possible to make $A$ a divisor of $B$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two integers $A$ and $B$.
### Output Format

For each test case, output `YES` if it is possible to make $A$ a factor of $B$, `NO` otherwise.

You can print each character of the string in uppercase or lowercase. For example, the strings `Yes`, `YES`, `yes`, and `yEs`, are all considered identical.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq A \leq B \leq 10^9$
### Sample 1:
Input
Output

```
3
3 6
4 14
9 10

```

```
YES
YES
NO

```

### Explanation:

 **Test case $1$:**  We can choose $X = 0$ and add them to $3$ and $6$. Thus, $3$ is a factor of $6$.

 **Test case $2$:**  We can choose $X = 1$ and add them to $4$ and $14$. Thus, $4+1 = 5$ is a factor of $14+1 = 15$.

 **Test case $3$:**  There is no possible value of $X$ to add such that $A$ becomes a factor of $B$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-13T14:27:00.612Z  

```py
# cook your dish here
T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    if A==B or B>=2*A: 
        print("YES")
    else:
        print("NO")
 
```

---

[View on CodeChef](https://www.codechef.com/problems/MAKEMULTIPLE)