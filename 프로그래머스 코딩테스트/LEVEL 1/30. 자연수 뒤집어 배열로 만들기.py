def solution(n):
    n=str(n)
    n=n[::-1]

    return list(map(int, (x for x in n)))

def solution2(n):
    return list(map(int, reversed(str(n))))
n=12345
print(solution(n))