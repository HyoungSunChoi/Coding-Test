'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

n=int(input())
cnt=0
for _ in range(n):
    word=input()
    stack=[]
    for x in word:
        if not stack:
            stack.append(x)
        elif x==stack[-1] or x not in stack:
            stack.append(x)
    if len(stack)==len(word):
        cnt+=1
print(cnt)
'''
result=0
for i in range(int(input())):
    word=input()
    if list(word)==sorted(word,key=word.find):
        # 입력된 단어의 리스트와, 알파벳 기준 순서대로 정렬했을 때 동일하다면? 그룹단어!!!
        result+=1
print(result)