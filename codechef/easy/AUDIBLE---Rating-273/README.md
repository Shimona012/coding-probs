# AUDIBLE - Rating 273

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-29T14:50:36.599Z  

```c_cpp
#include <stdio.h>

int main() {
	// your code goes here
	int N,M,T,i;
	scanf("%d",&T);
	for (i=0;i<T;i++){
	    scanf("%d",&N);
	    scanf("%d",&M);
	    if (N<=M) printf("%d",0);
	    else printf("%d",N-M);
	    printf("\n");
	}
	return 0;

}


```

---

[View on CodeChef](https://www.codechef.com/problems/AUDIBLE)