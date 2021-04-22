def solution(arr):
    if len(arr)>1:
        arr.remove(min(arr))
        return arr
    return [-1]
arr=[2,3,4,1]
print(solution(arr))