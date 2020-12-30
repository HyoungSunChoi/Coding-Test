'''
알파벳 소문자로만 이루어진 단어 S가 주어진다.
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
소문자 a~z
'''
# 방법 1
s=input()
lst=[]
for i in s:
    lst.append(i)
for i in range(97,123):
    if chr(i) in lst:
        print(lst.index(chr(i)),end=' ')
    else:
        print(-1,end=' ')
# 방법 2
# find 함수사용
word=input()
alpha=list(range(97,123))
for x in alpha:
    print(word.find(chr(x)),end=' ')

'''
find, index 함수 사용해보기

단어 'oxoxox' 에서 문자 x 가 첫번째 위치한 자리 출력
변수.find(찾을 문자)                   / 변수.index(찾을 문자)
        1                                      1

변수의 1~3번째 사이에 'o'가 위치한 자리    2번째 위치부터 처음 'x'가 위치한 자리        
    변수.find('o',1,3)                  'oxoxox'.index('x',2) -> 3
      없으면 -1 반환                         없으면 aTTRIBUTEeRROR 발생

'''