def solution(s):
    x=list(map(str,s.split()))
    res=''
    for word in x:
        new_word=''
        for i in range(len(word)):
            new_word+=word[i].upper() if i%2==0 else word[i].lower()
        res+=new_word+' '
    return res
s='try hello world'
print(solution(s))
