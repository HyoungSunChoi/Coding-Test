'''
알파벳 대소문자로 된 단어가 주어지면,
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
'''
'''
# 답이 나오긴 나옴
        word=input()
        new_word=word.lower()
        new_word=list(map(str,new_word))
        stack=[]
        ans = -1
        for i in range(len(new_word)):
            cnt=0
            for j in range(i+1,len(new_word)):
                if new_word[i]==new_word[j]:
                    cnt+=1
            if ans<cnt:
                ans=cnt
                if len(stack)==0:
                    stack.append(new_word[i])
                elif new_word[i] not in stack:
                    stack.pop()
                    stack.append(new_word[i])
            elif ans==cnt:
                stack.append(new_word[i])
        if len(stack)>1:
            print('?')
        else:
            tmp=stack[0]
            print(tmp.upper())


# Counter 함수 활용 -> 런타임에러
        from collections import Counter
        word=input()
        word=word.upper()
        a=Counter(word).most_common(2)
        if a[0][1]==a[1][1]:
            print('?')
        else:
            ans=a[0][0]
            print(ans.upper())
'''
# 인터넷 배낀 방법
word=input().upper()
t=[]
for i in set(word):
    t.append(word.count(i))
idx=[i for i,x in enumerate(t) if x==max(t)] #최대값의 idx 값 찾기
if len(idx)>1: print('?')
else: print(list(set(word))[t.index(max(t))])