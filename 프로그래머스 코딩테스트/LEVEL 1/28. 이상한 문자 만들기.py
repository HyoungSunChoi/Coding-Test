def solution(s):
    res=''
    ch=0
    for i in range(len(s)):
        if s[i]!=' ':
            res+=s[i].upper() if ch%2==0 else s[i].lower()
            ch+=1
        else:
            res+=' '
            ch=0
    return res


s='try hello world'
print(solution(s))