# 가장 끝자리에 있는 원소 제외하고 정렬시키는 방법
def bubble_sort(data):
    for idx in range(len(data)-1):
        for idx2 in range(len(data)-idx-1):
            if data[idx2]<data[idx2+1]:
                data[idx2],data[idx2+1]=data[idx2+1],data[idx2]

# 조금더 개선된 알고리즘 ( swap 이 일어나지 않았다면? 바로 종료)
def bubble_sort_ver2(data):
    for idx in range(len(data)-1):
        swap=False
        for idx2 in range(len(data)-idx-1):
             if data[idx2]<data[idx2+1]:
                data[idx2],data[idx2+1]=data[idx2+1],data[idx2]
                swap=True
        if swap==False:
            break
    return data

import random
data_list = random.sample(range(100),10)
print(data_list, end=' ')

print(bubble_sort_ver2(data_list))