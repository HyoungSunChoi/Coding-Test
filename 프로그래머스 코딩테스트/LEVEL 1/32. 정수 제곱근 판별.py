def solution(n):
    a=list(x**2 for x in range(1,int(50000000000000**0.5)))
    if n in a:
        return int(((n**0.5)+1)**2)
    return -1

def solution2(n):
    from math import sqrt
    return 'no' if sqrt(n)%1 else int((sqrt(n)+1)**2)
print(solution2(121))