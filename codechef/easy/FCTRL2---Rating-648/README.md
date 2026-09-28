# FCTRL2 - Rating 648

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Small factorials

You are asked to calculate factorials of some small positive integers.

### Input

An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1 <= n <= 100

### Output

For each integer n given at input, display a line with the value of n!

 **Note:**  For larger numbers, their factorial can overflows any available numeric data type in C.

### Sample 1:
Input
Output

```
4
1
2
5
3
```

```
1
2
120
6
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-28T17:56:56.969Z  

```py
# cook your dish here
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
t=int(input())
for i in range(t):
    n=int(input())
    print(factorial(n))
    
```

---

[View on CodeChef](https://www.codechef.com/problems/FCTRL2)