def solution(a,b):
    return [[c+d for c,d in zip(a,b)] for a,b in zip(a,b)]