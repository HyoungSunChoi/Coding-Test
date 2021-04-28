'''
문제)
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M 번 더하여 가장 큰 수를 만드는 법칙
단. 배열의 특정 인덱스에 해당하는 수가 연속해서 K 번 초과하여 더해질 수 없다.
    서로 다른 인덱스에 해당하는 수가 같은 경우, 서로 다른 것으로 간주한다.
ex) [2,4,5,4,6] M=8 이고 K=3
6+6+6+5+6+6+6+5

첫째 줄에 N,M,K 가 주어진다.
둘째 줄에 N 개의 자연수가 주어진다
'''
'''m,k=map(int,input().split())
n=list(map(int,input().split()))
n.sort(reverse=True)
result=0
while m>0:
    result+= n[0]*k
    m-=k
    result+=n[1]
    m-=1
print(result)
'''

def solution(n,m,k):
    n.sort(reverse=True)
    print(n)
    count= int(m/(k+1))*k + m%(k+1)
    result=0
    result+=(count * n[0])+ (m-count)*n[1]
    return result
n=[2,4,5,4,6]
print('정답은',solution(n,8,3))