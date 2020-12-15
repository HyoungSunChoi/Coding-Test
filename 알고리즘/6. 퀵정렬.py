'''
1. 퀵 정렬(Quick Sort)이란?
    - 정렬 알고리즘의 꽃
    - 기준점(pivot 이라고 부름) 을 정하여 , 기준보다 낮은건 왼쪽, 높은건 오른쪽
    - 각 왼쪽, 오른쪽은 재귀함수를 활용하여 동일 함수 호출
    - 리턴

'''

'''# 대표적인 코딩!!!
def qsort(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return qsort(left) + [pivot] + qsort(right)
'''
'''
#list comprehension 사용
def qsort(data):
    if len(data)<=1:
        return data
    left, right=list(),list()
    pivot=data[0]

    left=[item for item in data[1:] if item<pivot]
    right=[item for item in data[1:] if item>=pivot]
    return qsort(left)+[pivot]+qsort(right)

import random
data_list = random.sample(range(100), 10)
print(qsort(data_list))
'''

def quick_sort(data):
    if len(data)<=1:
        return data
    left,right=list(),list()
    pivot=data[0]
    for index in range(1,len(data)):
        if data[index]<pivot:
            left.append(data[index])
        else:
            right.append(data[index])
    return quick_sort(left)+[pivot]+quick_sort(right)

    
    left = [item for item in data[1:] if item<pivot]
    right = [item for item in data[1:] if item>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)