# 주어진 수 3개 더했을 때 소수가 되는 경우의 개수
from itertools import combinations
def prime_number(x):
    answer=0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])