'''
한 마을에 모험가가 N 명
각 모험가 대상으로 공포도 측정
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다
ex)
N=5 이고 각 모험가의 공포도 [2,3,1,2,2]
그룹 1에 공포도가 1,2,3
그룹 2에 공포도가 2,2
총 최대 그룹 수 2가지
'''
n=int(input())
data=list(map(int,input().split()))
data.sort()
groups=0
count=0
for i in data:
    count+=1
    if count>=i:
        groups+=1
        count=0
print(groups)