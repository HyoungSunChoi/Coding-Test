'''
1. 대기 목록의 가장 앞 문서를 꺼낸다
2. 대기 목록 중 J 보다 높은 중요도가 있으면 J 를 가장 마지막으로
3. 그렇지 않으면 J를 인쇄
ex.) A, B, C ,D  중요도 [ 2 , 1, 3 , 2]
B C D A
C D A B
'''
from collections import deque
def solution(priorities, location):
    q=printing(priorities)
    for i in q:
        if i[0]==location:
            res=i
    print('결과는',res)
    answer= q.index(res)+1
    return answer

def printing(priorities):
    q=deque()
    for idx, num in enumerate(priorities):
        q.append([idx,num])
    while any(q[0][1]<q[i][1] for i in range(1,len(q))):
        tmp=q.popleft()
        q.append(tmp)
    print(q)
    return q



priorities=[3,4,5,6,7,2,7,6,9]
print(solution(priorities,3))