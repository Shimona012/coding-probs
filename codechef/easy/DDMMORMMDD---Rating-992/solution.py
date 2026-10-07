t = int(input())

while t > 0:
    s = input().strip()
    dates=s.split("/")
    if int(dates[0])<32 and int(dates[1])<13:
        if int(dates[0])<13 and int(dates[1])<32:
            print("BOTH")
        else:
            print("DD/MM/YYYY")
    else:
        print("MM/DD/YYYY")
        
    t -= 1
