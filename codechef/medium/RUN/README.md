# RUN

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Run Anjali Run

 

Anjali is given a Distance M to run from one place to another place. Due to her asthma problem, at ith day she can run up to at most X distance. Suppose there are N days in a year. Assume she run optimally, you need to output the minimum day number to reach the destination

 

### Input

The first input line contains the  **T**  number of test cases. Each testcase consist of three lines First line consist of single integer  **N**  — the number of days in a year.
Next line contains  **N**  non-negative space-separated numbers— i.e. distance which Anjali will run on ith day. At least one of the numbers is greater than zero.
And the third line consist of the value of total Distance  **M**  which Anjali has to cover.

 

### Output

For each testcase you need to output the answer to the following query.

 

### Constraints

- 1<=T<= 10
- 1<=N<=10^5
- 0<=X<=10^8
- 0<=M<=10^16

 

### Example

```
Input:
2
5
1 5 0 0 2
9
3
1 3 0
2
Output:
1
2

```

 

### Explanation

For first testcase distance M is 9 units.
On the 1st day distance covered is 1 unit.
On the 2nd day distance covered is 5 units.
On 3rd and 4th day distance covered is 0 units.
On the 5th day distance covered is 2 units.
So total distance covered till 5th day is 8 units.
Then she will go to the first day of the next year.
So total distance covered till 1st day will be 9 units.
So answer is 1.

Similarly answer for second testcase is 2.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T18:08:56.970Z  

```py
T=input()
for i in range(int(T)):
    N=int(input())
    info=list(map(int,input().split()))
    M=float(input())
    total = sum(info)
    M%=total
    if M==0:
        M=total
    sumD=0
    for i in range(N):
        sumD+=info[i]
        if sumD>=M:
            print(i+1)
            break
        
```

---

[View on CodeChef](https://www.codechef.com/problems/RUN)