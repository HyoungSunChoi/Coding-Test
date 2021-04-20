def solution(arr,divisor):
    cnt=0
    answer = []
    for x in arr:
        if x%divisor==0:
            cnt+=1
            answer.append(x)
    answer.sort()
    if cnt==0:
        return [-1]
    return answer
