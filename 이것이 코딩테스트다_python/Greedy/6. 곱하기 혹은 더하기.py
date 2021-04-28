'''
문자열 S
숫자 사이에 X 혹은 + 연산자를 넣어 가장 큰 수
단 모든 연산은 왼쪽부터 순서대로
ex) 02984 문자열이 주어지면
0+2 * 9 * 8 * 4
'''
s=input()
result=int(s[0])
for i in range(1,len(s)):
    num=int(s[i])
    if num<=1 or result<=1:
        result+= num
    else:
        result *= num
print(result)