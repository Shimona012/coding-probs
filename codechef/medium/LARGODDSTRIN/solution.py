def findLargestOddSubstring(num):
    num+='0'
    count=''
    max_count=''
    for i in num:
        count+=i
        if int(count)%2==0:
            if len(count)>=len(max_count):
                max_count=count
                count=''

    if max_count=='':
        return -1
    else:
        return max_count
    
