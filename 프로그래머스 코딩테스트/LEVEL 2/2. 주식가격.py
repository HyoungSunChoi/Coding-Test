def solution(prices):
    x=len(prices)
    ch=[0]*x
    for i in range(x-1):
        for j in range(i,x-1):
            if prices[i]>prices[j]:
                print(prices[i],prices[j],'break')
                break
            else:
                ch[i]+=1
            print(ch,i,j)
    return ch


# 큐로 풀어보자;
from collections import deque
def solution2(prices):
    prices=deque(prices)
    result=[]
    while prices:
        time=0
        price = prices.popleft()
        for i in prices:
            time+=1
            if price>i:
                break
        result.append(time)
    return result


prices=[1,2,3,2,3]
print(solution2(prices))