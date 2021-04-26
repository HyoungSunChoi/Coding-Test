'''
aabbaccc 의 경우 -> 2a2ba3c

abcabcdede 의 경우 -> 문자열 압축 안됨

개선안
ababacdcd -> 2ab2cd
'''
def solution(s):
    length=[]
    result=''
    if len(s)==1:
        return 1

    for cut in range(1,len(s)//2+1):
        count=1
        tmp=s[:cut]
        print(tmp,cut)
        for i in range(cut,len(s),cut):
            if s[i:i+cut]==tmp:
                count+=1
            else:
                if count==1:
                    count=''
                result += str(count)+tmp
                tmp=s[i:i+cut]
                count=1
        if count==1:
            count=''
        result+=str(count)+tmp
        print(result)
        length.append(len(result))
        result=''
    return min(length)


s='aabbaccc'
print(solution(s))
