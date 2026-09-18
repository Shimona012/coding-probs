# CHFINTRO - Rating 951

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Interactive Contests

"Every beginning has an end... and an editorial." - taran_1407

What the hell are all these interactive problems? What does flushing output mean? So many questions... Chef explains it in an easy way: you must communicate with a grader program, which accepts your input only if you flushed the output.

There is a contest with interactive problems where $N$ people participate. Each contestant has a known rating. Chef wants to know which contestants will not forget to flush the output in interactive problems. Fortunately, he knows that contestants with rating at least $r$ never forget to flush their output and contestants with rating smaller than $r$ always forget to do it. Help Chef!

### Input
- The first line of the input contains two space-separated integers $N$ and $r$.
- Each of the following $N$ lines contains a single integer $R$ denoting the rating of one contestant.
### Output

For each contestant, print a single line containing the string `"Good boi"` if this contestant does not forget to flush the output or `"Bad boi"` otherwise.

### Constraints
- $1 \le N \le 1,000$
- $1,300 \le r, R \le 1,501$
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
2 1500
1499
1501
```

```
Bad boi
Good boi
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T12:06:58.912Z  

```py
# cook your dish here
N,r=input().split()
for i in range(int(N)):
    R=int(input())
    if R<int(r):
        print("Bad boi")
    else:
        print("Good boi")

```

---

[View on CodeChef](https://www.codechef.com/problems/CHFINTRO)