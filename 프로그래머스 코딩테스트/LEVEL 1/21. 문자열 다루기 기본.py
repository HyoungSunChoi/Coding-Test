def solution(s):
    if s.isdigit():
        if len(s)==4 or len(s)==6:
            return True
    return False
s='1234'
print(solution(s))