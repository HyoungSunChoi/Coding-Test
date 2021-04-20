s='ZbjaoA'
def solution(s):
    res=''
    answer=sorted(s,reverse=True)
    for x in answer:
        res+=str(x)
    return res


def solution2(s):
    return ''.join(sorted(s,reverse=True))