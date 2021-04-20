def solution(a,b):
    if a<b:
        return sum([i for i in range(a,(b+1))])
    return sum([i for i in range(b,(b+1))])

