# CLEARDAY - Rating 233

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Clear Day

Chef classifies a day to be either `rainy`, `cloudy`, or `clear`.

In a particular  **week**, Chef finds $X$ days to be `rainy` and $Y$ days to be `cloudy`.
Find the number of `clear` days in the week.

### Input Format
- The first and only line of input will contain two space-separated integers $X$ and $Y$, denoting the number of rainy and cloudy days in the week.
### Output Format

Output the number of clear days in the week.

### Constraints
- $0 \leq X, Y \leq 7$
- $0 \leq X+Y \leq 7$
### Sample 1:
Input
Output

```
2 3
```

```
2
```

### Explanation:

There are $7$ days in a week. If there are $2$ rainy days and $3$ cloudy days, then the remaining $7-2-3=2$ days are clear.

### Sample 2:
Input
Output

```
3 4
```

```
0
```

### Explanation:

If there are $3$ rainy days and $4$ cloudy days, then the remaining $7-3-4=0$ days are clear.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T16:18:24.778Z  

```c_cpp
#include <stdio.h>

int main() {
	// your code goes here
    int X,Y,clear;
    scanf("%d",&X);
    scanf("%d",&Y);
    clear=7-X-Y;
    printf("%d",clear);
    return 0;
}


```

---

[View on CodeChef](https://www.codechef.com/problems/CLEARDAY)