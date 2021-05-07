'''
알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어진다.
이때 모든 알파벳을 오름차순으로 정렬하여 출력한 후 모든 숫자를 더한 값 출력
ex) K1KA5CB7 이 입력되면 ABCKK13 출력
'''
s=input()
res=0
word=[]
for x in s:
    if x.isdigit():
        res+=int(x)
    else:
        word.append(x)
word.sort()
answer=''.join(i for i in word)
answer+=str(res)
print(answer)
