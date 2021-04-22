def solution(n):
    x = sorted(map(str, (x for x in str(n))), reverse=True)
    return int(''.join(x))


def solution2(n):
    return int(''.join(sorted(str(n), reverse=True)))


n = 118372
print(solution2(n))
