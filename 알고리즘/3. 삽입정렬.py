'''
# 삽입 정렬( insertion sort) 란?
    - 1. 삽입 정렬은 2번째 인덱스부터 시작
    - 2. 해당 인덱스(key 값) 앞에 있는 데이터부터 비교해서 key 값이 더 작으면 데이터값을 뒤 인덱스로 복사
    - 3. 이름 key 값이 더 큰 데이터를 만날때까지 반복,
'''


def insertion_sort(data):
    for idx in range(len(data) - 1):
        for idx2 in range(idx + 1, 0, -1):
            if data[idx2] < data[idx2 - 1]:
                data[idx2], data[idx2 - 1] = data[idx2 - 1], data[idx2]
            else:  # 만약 스왑을 하지 않았다면
                break  # 그 턴은 종료시킨다.
    return data

import random
data_list = random.sample(range(100),10)
print(data_list, end=' ')
print()
print(insertion_sort(data_list))