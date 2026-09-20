# CHFNUM

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef and The Number

Chef on learning about various types of numbers, wanted to discover his own type of number where if a positive whole number 'n' has 'd' digits then if the square of that number is divided into 2 pieces of either consisting of 'd' or 'd-1' digits and when the two pieces are added together, we get back the original number 'n'.

Chef has theorized the concept and has determined some numbers that follow this property he wants you to check whether they really do or not.

### Input
The number 'n'.

### Output
Output as  **yes**  if the number follows the property else output as  **no**.

### Example

```
Input:
9
Output:
yes

```

### Explanation

92 = 81

Left hand piece of 81 = 8

Right hand piece of 81 = 1

Addition of both the pieces (8 + 1) = 9 i.e. the original number.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T06:19:37.923Z  

```py
# cook your dish here
n=input()
d=len(n)

num=str(int(n) ** 2)

p1=int(num[:d])
try:
    p2=int(num[d:])
except ValueError:
    p2=0
if d>1:
    p3=int(num[:d-1])
else:
    p3=0
try:
    p4=int(num[d-1:])
except:
    p4=0

if p1+p2==int(n) or p3+p4==int(n):
    print("yes")
else:
    print("no")
```

---

[View on CodeChef](https://www.codechef.com/problems/CHFNUM)