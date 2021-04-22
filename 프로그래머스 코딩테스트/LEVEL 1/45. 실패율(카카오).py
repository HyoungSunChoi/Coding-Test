# 전체 스테이지 개수 N
# 게임 이용하는 사용자가 멈춰있는 스테이지의 번호가 담긴 배열 stages
def solution(N,stages):
    # 실패율 : 현재 스테이지 클리어 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
    # 실패율 : ex) 3스테이지 실패율
                # stage==3 / stage>=3
    answer = []
    for i in range(1,N+1):
        access=0
        fail=0
        for stage in stages:
            if stage>=i:
                access+=1
            if stage==i:
                fail+=1
        if access==0:
            answer.append((i,0))
        answer.append((i,fail/access))
    answer.sort(key=lambda x:x[1],reverse=True)
    res=[]
    for x in answer:
        res.append(x[0])
    return res


stages=[2,1,2,6,2,4,3,3]
print(solution(5,stages))