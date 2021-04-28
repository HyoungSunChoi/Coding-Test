'''
N X N 크기의 정사각형 공간
가장 왼쪽 위 좌표는 (1,1) 이며 가장 오른쪽 아래 좌표는 (N,N) 이다
A 는 상,하,좌,우 방향으로만 이동할 수 있다.
     U,D, L, R
지도 밖을 넘어가는 경우에는 무시
공간의 크기와 방향이 주어진다.

'''

n=int(input())
x,y=1,1
plans=input().split()

dx=[0,0,1,-1]
dy=[1,-1,0,0]
move_types=['R','L','D','U']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny
print(x,y)





