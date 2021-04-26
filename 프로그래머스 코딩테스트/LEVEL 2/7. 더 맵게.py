import heapq

def solution(scovile,k):
    heap=[]
    for x in scovile:
        heapq.heappush(heap,x)
    cnt=0
    while heap[0]<=k:
        try:
            heapq.heappush(heap, (heapq.heappop(heap)+(heapq.heappop(heap)*2)) )
        except IndexError:
            return -1
        cnt+=1
    return cnt

scovile=[1,2,3,9,10,12]
k=7
print(solution(scovile,k))