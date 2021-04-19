# 전체 학생 수 n, 체육복 도난당한 학생 lost , 여벌 학생 reserve
# 체육수업 들을 수 있는 학생의 최댓값

def solution(n,lost,reserve):
    set_reserve=set(reserve)-set(lost)
    set_lost=set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)