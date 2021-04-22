arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
n=5


def solution(n,arr1,arr2):
    new_1=[]
    new_2=[]
    for x in arr1:
        new_1.append(change(n,x))
    for x in arr2:
        new_2.append(change(n, x))
    res=add(new_1,new_2)
    result=['']*n
    for i in range(n):
        for j in range(n):
            if res[i][j]==0:
                result[i]+=' '
            else:
                result[i]+='#'
    return result
# 행렬 덧셈 함수
def add(a,b):
    return [[c+d for c,d in zip(a,b)] for a,b in zip(a,b)]

# 2진수 변환 함수
def change(n,num):
    res=[]
    ch=0
    while num>=1:
        res.append((num%2))
        num//=2
        ch+=1
    if ch==n:
        return res[::-1]
    while ch!=n:
        res.append(0)
        ch+=1
    return res[::-1]

solution(n,arr1,arr2)