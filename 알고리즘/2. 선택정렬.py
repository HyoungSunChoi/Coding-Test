'''
2. 선택정렬 (selection sort) 란?
    - 1. 주어진 데이터 중, 최소값을 찾음
    - 2. 해당 최소값을 데이터 맨 앞 위치한 값과 교체
    - 3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 교환
'''


def selection_sort(data):
    for idx in range(len(data) - 1):  # 1을 빼야하는 이유 -> 전체 횟수는 총 길이 -1 번만큼 반복한다
        lowest = idx
        for idx2 in range(idx + 1, len(data)):  # 두번째부터~ 끝까지
            if data[lowest] > data[idx2]:
                lowest = idx2
        data[lowest], data[idx] = data[idx], data[lowest]
    print(data)


import random
data_list = random.sample(range(100),10)
print(data_list, end=' ')