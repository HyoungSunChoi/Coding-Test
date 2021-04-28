'''
1이 될 때까지 2가지 방법을 선택한다

1. N 에서 1을 뺀다
2. N 을 K 로 나눈다. (단 나누어 떨어질 때)
'''

'''
방법1 
n,k=map(int,input().split())
cnt=0
while n!=1:
    if n%k==0:
        cnt+=1
        n//=k
    else:
        n-=1
        cnt+=1
print(cnt)
'''

# 방법 2
# 바로 연산 때려버리기
import math
n,k=map(int,input().split())
cnt=0
while n%k!=0:
    print(n)
    cnt+=1
    n-=1

print(int(n**(1/k)))
print(cnt)