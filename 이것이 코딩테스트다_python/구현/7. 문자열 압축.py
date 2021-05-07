'''
문자열 압축하는 방법
aabbaccc 는 2a2ba3c 로 압축될 수 있으나 압축률이 낮다
abcabcdede
'''

def solution(s):
    answer=len(s)
    for step in range(1,len(s)//2+1):
        compressed=''
        tmp=s[:step]
        count=1
        for i in range(step,len(s),step):
            if tmp==s[i:i+step]:
                count+=1
            else:
                compressed+=str(count)+tmp if count>=2 else tmp
                tmp=s[i:i+step]
                count=1
        compressed+=str(count)+tmp if count>=2 else tmp
        answer=min(answer,len(compressed))
    return answer


