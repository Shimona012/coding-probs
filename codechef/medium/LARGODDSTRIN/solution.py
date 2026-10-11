def findLargestOddSubstring(num):
    num+='0'
    count=''
    max_count=''
    for i in num:
        if int(i)%2==0:
            if len(count)>=len(max_count):
                max_count=count
                count=''
        else:
            count+=i
    if max_count=='':
        return -1
    else:
        return max_count
    
