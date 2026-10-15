# VOTERS - Rating 1114

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Discrepancies in the Voters List

As you might remember, the collector of Siruseri had ordered a complete revision of the Voters List. He knew that constructing the list of voters is a difficult task, prone to errors. Some voters may have been away on vacation, others may have moved during the enrollment and so on.

To be as accurate as possible, he entrusted the task to three different officials. Each of them was to independently record the list of voters and send it to the collector. In Siruseri, every one has a ID number and the list would only list the ID numbers of the voters and not their names. The officials were expected to arrange the ID numbers in ascending order in their lists. Voter ID numbers are unique and not duplicated in any lists.

On receiving the lists, the Collector realised that there were discrepancies - the three lists were not identical. He decided to go with the majority. That is, he decided to construct the final list including only those ID numbers that appeared in at least 2 out of the 3 lists. For example if the three lists were

```
23  30  42  57  90
21  23  35  57  90  92
21  23  30  57  90 

```

then the final list compiled by the collector would be:

```
21  23  30  57  90

```

The ID numbers 35, 42 and 92 which appeared in only one list each do not figure in the final list.

Your task is to help the collector by writing a program that produces the final list from the three given lists.

Input format

The first line of the input contains 3 integers  *N* 1,  *N* 2 and  *N* 3.  *N* 1 is the number of voters in the first list,  *N* 2 is the number of voters in the second list and  *N* 3 is the number of voters in the third list. The next  *N* 1 lines (lines 2,..., *N* 1+1) contain one positive integer each and describe the first list in ascending order. The following

 *N* 2 lines (lines  *N* 1+2,..., *N* 1+ *N* 2+1) describe the second list in ascending order and the final  *N* 3 lines (lines

 *N* 1+ *N* 2+2,..., *N* 1+ *N* 2+ *N* 3+1) describe the third list in ascending order.

Output format

The first line of the output should contain a single integer  *M*  indicating the number voters in the final list. The next  *M*  lines (lines 2,..., *M* +1) should contain one positive integer each, describing the list of voters in the final list, in ascending order.

Test data

You may assume that 1 ≤  *N* 1, *N* 2, *N* 3 ≤ 50000.

### Sample 1:
Input
Output

```
5 6 5
23
30
42
57
90
21 
23 
35 
57 
90 
92 
21 
23 
30 
57 
90 
```

```
5
21 
23 
30 
57 
90
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T18:14:57.728Z  

```py
N1,N2,N3=map(int,input().split())
voter_one,voter_two,voter_three=set(),set(),set()
for i in range(N1):
    vot_id=int(input().strip())
    voter_one.add(vot_id)
for j in range(N2):
    vot_id=int(input().strip())
    voter_two.add(vot_id)
for k in range(N3):
    vot_id=int(input().strip())
    voter_three.add(vot_id)
final_list=sorted((voter_one&voter_two)|(voter_two&voter_three)|(voter_one&voter_three))
print(len(final_list))
for voter in final_list:
    print(voter)
```

---

[View on CodeChef](https://www.codechef.com/problems/VOTERS)