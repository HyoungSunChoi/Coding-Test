from collections import deque

def BFS(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                print('현재 큐',queue)
                visited[i]=True
                print('현재 방문 상태',visited)
graph= [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False] * 9
BFS(graph,1,visited)