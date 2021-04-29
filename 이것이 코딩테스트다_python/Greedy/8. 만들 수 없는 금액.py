'''
N개의 동전으로 만들 수 없는 양의 정수 금액 중 최솟값을 구하라
ex) N=5 이고 동전이 각각 3,2,1,1,9 인 경우   만들 수 없는 최솟값은 8원이다.
    N=3 이고 동전이 각각 3,5,7 인 경우 만들 수 없는 최솟값은 1원
'''

n=int(input())
data=list(map(int,input().split()))
data.sort()

target=1
for x in data:
    if target<x:
        break
    target+=x
print(target)