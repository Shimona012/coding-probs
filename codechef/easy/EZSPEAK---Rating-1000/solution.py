vowels=['a','e','i','o','u']
T=int(input())
for i in range(T):
    N=int(input())
    S=list(input())
    if len(S)<4:
        print("YES")
    else:
        for j in range(len(S)-3):
            if all(let not in vowels for let in S[j:j+4]):
                print("NO")
                break
        else:
            print("YES")