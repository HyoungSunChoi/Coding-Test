'''
트럭 다리 건너는데 최단 몇 초인지 계산하기


조건.)
1. 트럭은 1초에 1만큼 움직인다.
2. 다리길이는 bridge_length
3. 다리는 weight 까지 견딘다

ex.) 길이가 2이고 10kg 무게를 견디는 다리가 있다.
무게가 [7,4,5,6] kg 인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 ?

'''
def solution(bridge_length, weight, truck_weights):
    time=0
    q=[0]*bridge_length
    while q:
        time+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return time
truck_wieghts=[7,4,5,6]
print(solution(2,10,truck_wieghts))
