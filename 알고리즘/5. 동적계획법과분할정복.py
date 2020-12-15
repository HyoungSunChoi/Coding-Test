'''
1. 정의
    1-1. 동적 계획법 (DP라고 불림)
        - 입력 크기가 작은 부분 문제들을 해결한 후, 해당 부분 문제의 해를 활용해서, 보다 큰 크기의 부분 문제를 해결 --> 최종적으로 전체 문제를 해결
        - 상향식 접근법 ( 가장 최하위 해답을 구하여, 이를 이용하여 상위 문제를 풀어가는 방식)
        - Memoization 기법 사용
            - Memoization : 프로그램 실행 시 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 하여 전체 실행 속도로를 빠르게 하는 기술
        - 문제를 잘게 쪼갤 때 부분 문제는 중복되어, 재활용됨
            ex.) 피보나치 수열
    1-2. 분할 정복
        - 문제를 나눌 수 없을 때 까지 나누어서 각각 풀면서 다시 합병하여 문제의 답을 얻는 알고리즘
        - 하양식 접근법, 상위의 해답을 구하기 위해 아래로 내려가면서 하위의 해답을 구함
            - 일반적으로 재귀함수로 구현
        - 문제를 잘게 쪼갤 때, 부분 문제는 서로 중복되지 않음
            ex.) 병합 정렬, 퀵 정렬

2. 공통점과 차이점
    - 공통점
        - 문제를 잘게 쪼개서, 가장 작은 단위로 분할
    - 차이점
        - 동적 계획법
            - 부분 문제는 중복되어, 상위 문제 해결 시 재활용됨

3. 동적 계획법 알고리즘 이해
'''

'''
# recursive call 활용
def fibo(num):
    if num<=1:
        return num
    else:
        return fibo(num-1)+fibo(num-2)
print(fibo(100))

# 동적 계획법 활용 (dp)
def fibo_dp(num):
    # memorization 사용
    cache = [0 for index in range(num+1)]
    # 캐시 메모리 생성
    cache[0]=0
    cache[1]=1
    for index in range(2,num+1):
        cache[index]=cache[index-1]+cache[index-2]
    return cache[num]
print(fibo_dp(4))
'''

