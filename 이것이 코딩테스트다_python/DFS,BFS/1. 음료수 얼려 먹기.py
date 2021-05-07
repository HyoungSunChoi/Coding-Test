'''
N X M 크기의 얼음 틀
구멍 뚫려 있는 부분 0, 칸막이가 졵재하는 부분 1
구멍이 뚫려있는 부분끼리, 상 / 하 / 좌 / 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
'''

n,m = map(int,input().split())
ice=[list(map(int,str(input()))) for _ in range(n)]
print(ice)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

count=0

def DFS(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if ice[x][y]==0:
        ice[x][y]=1
        for _ in range(4):
            DFS(x+dx[_],y+dy[_])
        return True
    return False
for i in range(n):
    for j in range(m):
        if DFS(i,j)==True:
            count+=1
print(count)
