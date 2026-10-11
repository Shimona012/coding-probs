# ANUUND - Rating 1198

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Ups and Downs
### Problem description

You will be given a zero-indexed array  **A**. You need to rearrange its elements in such a way that the following conditions are satisfied:

- A[i] ≤ A[i+1] if i is even.
- A[i] ≥ A[i+1] if i is odd.
In other words the following inequality should hold:  **A[0] ≤ A[1] ≥ A[2] ≤ A[3] ≥ A[4]**, and so on. Operations  **≤**  and  **≥**  should alter.
### Input

The first line contains a single integer  **T**  denoting the number of test cases. The first line of each test case contains an integer  **N**, that is the size of the array  **A**. The second line of each test case contains the elements of array  **A** 

### Output

For each test case, output a single line containing  **N**  space separated integers, which are the elements of  **A**  arranged in the required order. If there are more than one valid arrangements, you can output any of them.

### Constraints
- 1 ≤ N ≤ 100000
- Sum of N in one test file ≤ 600000
- 1 ≤ A[i] ≤ 10^9
### Sample 1:
Input
Output

```
2
2
3 2
3
10 5 2
```

```
2 3
2 10 5
```

### Explanation:

 **Example case 1.** 
 **A[0]**  ?  **A[1]**  is satisfied, 2 ? 3.

 **Example case 2.** 
 **A[0]**  ?  **A[1]**  is satisfied, 2 ? 10.
 **A[1]**  ?  **A[2]**  is satisfied, 10 ? 5.
 **Note:**  5 10 2 is also valid answer.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T17:50:35.630Z  

```py
# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    for i in range(1,N-1,2):
        A[i],A[i+1]=A[i+1],A[i]
    print(" ".join(map(str,A)))

```

---

[View on CodeChef](https://www.codechef.com/problems/ANUUND)