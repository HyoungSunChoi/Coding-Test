n,m =map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
def solution(a):
    res = 0
    for i in range(n):
        if min(a[i])>res:
            res=min(a[i])
    return res
print(solution(a))