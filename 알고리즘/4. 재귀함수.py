
# 일반적인 곱셈 함수
'''
def multiple(num):
    return_value=1
    for index in range(1,num+1):
        return_value=return_value * index
    return return_value
def multiple(num):
    if num<=1:
        return num
    return num * multiple(num-1)

print(multiple(5))
-> 120 출력

# 리스트의 합 구하기
def sum_list(data):
    if len(data)<=1:
        return data[0]
    return data[0]+sum_list(data[1:])

import random
data=random.sample(range(100),10)
print()


# 회문 문자열 슬라이싱으로 구분하기
string='Dave'
string[0]='D'
string[-1]='e'
string[1:-1]='av'
string[:-1]='Dav'


# 회문 문자열 재귀함수로 구현하기
def abc(data):
    if len(data)==1:
        return True
    if data[0]==data[-1]:
        return abc(data[1:-1])
    else:
        return False
'''

''' 
프로그래밍 연습
1. 정수 n에 대해
2. n이 홀수이면 3 * n+1을하고
3. n이 짝수이면 n을 2로 나눈다
4. 이렇게 해서 n 이 1이 될때까지 반복

def abc(data):
    print(data)
    if data<=1:
        return data

    if data%2==0:
        return abc(data/2)
    else:
        return abc(data*3+1)
print(abc(3))
'''

'''
프로그래밍 연습
문제 : 정수 4를 1,2,3의 조합으로 나타내는 방법은 7가지
1+1+1+1
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 입력으로 주어졌을 때, n을 1,2,3 의 합으로 나타낼 수 있는 방법의 수를 

def func(data):
    if data==1:
        return 1
    elif data==2:
        return 2
    elif data==3:
        return 4
    return func(data-1)+func(data-2)+func(data-3)
print(func(10))
'''


