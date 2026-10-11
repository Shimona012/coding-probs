def findLargestOddSubstring(num):
    count=''
    max_count=''
    for i in range(len(num)):
        if int(num[i])%2!=0:
            max_count=num[:i+1]
    if max_count=='':
        return -1
    else:
        return max_count
    
