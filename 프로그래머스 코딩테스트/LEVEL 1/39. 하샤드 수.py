def solution(x):
    ch=str(x)
    div=0
    for i in ch:
        div+=int(i)
    if x%div==0:
        return True
    return False

def solution2(x):
    return False if x%sum([int(i) for i in list(str(x))]) !=0 else True

print(solution(11))