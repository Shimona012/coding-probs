# CHEFARR

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef and array
### Problem Statement

Chef has an array of N numbers. Chef wants to know the number of ways to divide it into 3 contiguous parts such that the sum of the three parts is equal. Formally you need to find number of indices i,j such that sum of elements from 1 to i-1 = sum of elements from i to j = sum of elements from j+1 to N.

### Input

The first line contains an integer N. Then the next line has N integers denoting the array 'A'.

### Output

A single integer denoting the number of ways to split the array into 3 parts with equal sum.

### Constraints
- 1 <= N <= 5*105
- 0 <= |A[i]| <= 109

Note : The numbers might be negative.

### Example

```
Input 1:
5
1 2 3 0 3
Output 1:
2

```

```
Input 2:
4
0 1 -1 0
Output 2:
1

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T10:41:14.610Z  

```py
# cook your dish here
N=int(input())
A=list(map(int,input().split()))
count=0
ways=0
tot_sum=sum(A)
if tot_sum%3==0:
    small_sol=tot_sum//3
    big_sol=small_sol*2
    temp_sum=0
    for i in range(N-1):
        temp_sum+=A[i]
        if temp_sum==big_sol:
            ways+=count
        if temp_sum==small_sol:
            count+=1
        
    print(ways)
else:
    print(0)

```

---

[View on CodeChef](https://www.codechef.com/problems/CHEFARR)