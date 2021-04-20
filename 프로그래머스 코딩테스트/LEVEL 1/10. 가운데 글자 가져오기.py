'''def solution(s):
    answer=''
    s=list(map(str,s))
    if len(s)%2==0:
        s=s[len(s)//2-1:len(s)//2+1]
    else:
        s=s[len(s)//2:len(s)//2+1]
    for x in s:
        answer+=str(x)
    return answer

    return s[(len(s)-1)//2:]'''
s='abcde'
def solution(s):
    return s[(len(s)-1)//2:(len(s)//2)+1]
print(solution(s))