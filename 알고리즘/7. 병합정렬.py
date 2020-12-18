'''
병합 정렬
1. 리스트를 절반으로 잘라 비슷한 크기의 두개로 나눈다
2. 자른 부분을 또 자르고 정렬하여 합친다
3. 합친다

[1,9,3,2]
[1,9] , [3,2]

# 나누는 함수  - 분리하는 재귀함수
# 합치는 함수
'''


## 한번만 나누기
def split(data):
    if len(data) <= 1:
        return data
    med = int(len(data) / 2)
    left = data[:med]
    right = data[med:]
    print(left, right)


a = [1, 4, 3, 2, 5]

### 강의버전
def merge(left, right):
    lp = rp = 0
    lst = []
    # case 1 : left/right 아직 남아있는경우
    while len(left) > lp and len(right) > rp:
        if left[lp] > right[rp]:
            lst.append(right[rp])
            rp += 1
        else:
            lst.append(left[lp])
            lp += 1
    # case 2 : left 만 남아있는경우
    while len(left) > lp:
        lst.append(left[lp])
        lp += 1
    # case 3 : right 만 남아있는 경우
    while len(right) > rp:
        lst.append(right[rp])
        rp += 1
    return lst

### 내버전
def merge_ver2(left, right):
    lp=rp=0
    lst=[]
    while len(left)>lp and len(right)>rp:
        if left[lp]<=right[rp]:
            lst.append(left[lp])
            lp+=1
        else:
            lst.append(right[rp])
            rp+=1

    if len(left)>lp:
        lst=lst+left[lp:]
    else:
        lst=lst+right[rp:]
    return lst

# 분리하는 과정
def mergesplit(data):
    if len(data) <= 1:
        return data
    med = int(len(data) / 2)
    left = mergesplit(data[:med])
    right = mergesplit(data[med:])
    return merge_ver2(left, right)


import random
data_list= random.sample(range(100),10)
print(data_list)

print(mergesplit(data_list))