# PRIME1 - Rating 1620

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Prime Generator

Ram wants to generate some prime numbers for his cryptosystem. Help him please! Your task is to generate all prime numbers between two given numbers.

 **Warning: large Input/Output data, be careful with certain languages (though most should be OK if the algorithm is well designed)** 
### Input Format

The first line contains t, the number of test cases (less then or equal to 10).

Followed by t lines which contain two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

### Output Format

For every test case print all prime numbers p such that m <= p <= n, one number per line. Separate the answers for each test case by an empty line.

### Constraints

(1 <= m <= n <= 1000000000, n-m<=100000)

### Sample 1:
Input
Output

```
2
1 10
3 5
```

```
2
3
5
7
3
5
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-30T18:18:18.888Z  

```py
import sys
def is_prime(x):
    if x<=1:
        return False
    if x<=3:
        return True
    if x%2==0 or x%3==0:
        return False
    j=5
    while j*j<=x:
        if x%j==0 or x%(j+2)==0:
            return False
        j+=6
    return True
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    for x in range(m,n+1):
        if is_prime(x):
            print(x)
    print()
```

---

[View on CodeChef](https://www.codechef.com/problems/PRIME1)