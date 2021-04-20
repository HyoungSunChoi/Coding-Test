'''def solution(arr):
    answer=[]
    last=arr[0]
    answer.append(last)
    for x in range(1,len(arr)):
        if last==arr[x]:
            continue
        else:
            answer.append(arr[x])
            last=arr[x]
    return answer'''

def solution(arr):
    a=[]
    for i in arr:
        if a[-1:] ==[i]:
            continue
        a.append(i)
    return a
arr=[1,1,3,3,0,1,1]
print(solution(arr))