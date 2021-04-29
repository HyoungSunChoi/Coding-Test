'''
볼링공은 총 N 개, 무게는 1~M , 서로 다른 무게의 공을 들려고 할 때 경우의 수를 구하라
ex) N=5, M=3 , 무게가 1,3,2,3,2 일때 각 공의 번호가 차례대로 1~5번까지 주어진다
(1,2),(1,3),(1,4),(1,5),(2,3)(2,5)(3,4)(4,5)
'''

n,m=map(int,input().split())
ball=list(map(int,input().split()))
cnt=0
ball.sort()
for i in range(n):
    for j in range(i,n):
        if ball[i]!=ball[j]:
            cnt+=1
print(cnt)
