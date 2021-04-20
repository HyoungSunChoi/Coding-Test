def solution(n):
    ch=[True]*(n+1)
    # 에라토스테네스의 체
    for i in range(2,n+1):
        if ch[i]:
            for j in range(2*i,n+1,i):
                ch[j]=False
    a=[i for i in range(2,n+1) if ch[i]]
    return len(a)
print(solution(10))