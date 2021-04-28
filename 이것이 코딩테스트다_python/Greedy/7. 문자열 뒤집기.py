'''
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다.
문자열 S 에 있는 모든 숫자를 같게 만들려고 한다.
연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것
ex) S = 0001100 일때
전체를 뒤집으면 1110011이다
4번째~5번째 문자까지 뒤집으면 1111111이 되어 2번만에 모두 같은 숫자가 된다.
'''
s=input()
count0=0
count1=0
if s[0]=='1':
    count0+=1
else:
    count1+=1

for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        if s[i+1]=='1':
            count0+=1
        else:
            count1+=1
print(min(count0,count1))