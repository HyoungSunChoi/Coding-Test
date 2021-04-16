def solution(new_id):
    # 1단계:
    new_id=new_id.lower()
    # 2단계 :
    answer=''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer+=word
    # 3단계:
    while '..' in new_id:
        answer=answer.replace('..','.')
    # 4단계
    answer = answer[1:] if answer[0] =='.' and len(answer)>1 else answer
    answer=answer[:-1] if answer[-1] == '.' else answer
    # 5 단계
    answer='a' if answer=='' else answer
    # 6 단계
    if len(answer)>=16:
        answer=answer[:15]
        if answer[-1]=='.':
            answer=answer[:-1]
    if len(answer)<=3:
        answer=answer + answer[-1] * (3-len(answer))
    return answer

# 정규식 사용하기
import re
def solution(new_id):
    st=new_id
    st=st.lower()
    st=re.sub('[^a-z0-9\-_.]','',st)
    st=re.sub('\.+','',st)
    st=re.sub('^[.]|[.]$','',st)
    st='a' if len(st)==0 else st[:15]
    st=st if len(st)>2 else st+"".join([st[-1] for i in range(3-len(st))])
    return st