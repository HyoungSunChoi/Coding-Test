'''
N 마리의 폰켓못 중 N/2 마리 가져갈 수 있다.
가져갈 수 있는 최대의 종류의 포켓몬
from collections import Counter
def solution(nums):
    b=Counter(nums)
    if len(nums)//2 >=len(b):
        return len(b)
    return len(nums)//2
'''
def solutions(nums):
    return min(len(nums)/2, len(set(nums)))