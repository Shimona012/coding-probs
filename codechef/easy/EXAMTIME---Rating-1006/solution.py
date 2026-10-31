# cook your dish here
T=int(input())
for i in range(T):
    Dragon=list(map(int,input().split()))
    Sloth=list(map(int,input().split()))
    if sum(Dragon)==sum(Sloth):
        if Dragon[0]==Sloth[0]:
            if Dragon[1]==Sloth[1]:
                print("TIE")
            else:
                if Dragon[1]>Sloth[1]:
                    print("DRAGON")
                else:
                    print("SLOTH")
        else:
            if Dragon[0]>Sloth[0]:
                print("DRAGON")
            else:
                print("SLOTH")
    else:
        if sum(Dragon)>sum(Sloth):
            print("DRAGON")
        else:
            print("SLOTH")