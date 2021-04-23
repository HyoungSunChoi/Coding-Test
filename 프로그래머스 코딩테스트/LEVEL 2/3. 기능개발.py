'''
조건.)
1. 작업의 진도가 적힌 정수 배열 progresses, 각 작업 속도 speeds
2. 앞에 있는 기능보다 먼저 개발 가능 단, 배포시에는 앞에 있는 기능과 함께 배포
3. 각 배포날짜에 배포되는 개수 return
'''
from collections import deque
def solution(progresses, speeds):
    answer=[]
    progresses_left=[100]*len(progresses)
    pro_left=[ a-b for a,b in zip(progresses_left,progresses)]
    work_days=deque( a//b if a%b==0 else a//b+1 for a,b in zip(pro_left,speeds))

    print(work_days)
    print(work_days[0])
    while work_days:
        work_days=deque(x-1 for x in work_days)
        print(work_days)
        if work_days[0]==0:
            cnt=1
            work_days.popleft()
            while work_days and work_days[0]<=0:
                work_days.popleft()
                cnt+=1
            print(work_days)
            answer.append(cnt)
    return answer


progresses=[95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses,speeds))