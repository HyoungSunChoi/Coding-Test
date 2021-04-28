'''
문제)
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 동전이 있다.
손님에게 거슬러 줘야 할 돈이 N원일 때 동전의 최소의 개수를 구하라.

문제 해결)
가장 큰 화폐 단위부터 제공

주의)
* 해법이 정당한지 검토할 것
'''
def solution(money):
    cnt=0
    change=[500,100,50,10]
    for i in change:
        cnt+=money//i
        money=money%i
    return cnt
print(solution(1260))
