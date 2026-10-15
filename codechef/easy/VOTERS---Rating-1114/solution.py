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