# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    songs=list(map(int,input().split()))
    K=int(input())-1
    len_K=songs[K]
    songs.sort()
    print(songs.index(len_K)+1)
    
