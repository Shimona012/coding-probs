# Python If-Else

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/python-arithmetic-operators/tutorial) tab to know how to to solve.</sub>  

**Task**  
The provided code stub reads two integers from STDIN, $a$ and $b$.  Add code to print three lines where: 
<ol>

<li> The first line contains the sum of the two numbers. </li>  
<li> The second line contains the difference of the two numbers (first - second). </li>  
<li> The third line contains the product of the two numbers. </li>  
</ol>

**Example**  
$a = 3$  
$b = 5$  

Print the following:
<pre>
8
-2
15
</pre>

**Input Format**

The first line contains the first integer, $a$.  
The second line contains the second integer, $b$.  

**Constraints**

$1 \le a \le 10^{10}$  
$1 \le b \le 10^{10}$  
 

**Output Format**

Print the three lines as explained above.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T01:54:01.132Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2==0:
        if n>1:
            if n<6:
                print("Not Weird")
            elif n<21:
                print("Weird")
            else:
                print("Not Weird")
    else:
        print("Weird")

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem)