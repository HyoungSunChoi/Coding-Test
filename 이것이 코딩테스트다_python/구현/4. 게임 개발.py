'''
N X M 크기의 직사각형
각 칸은 육지/바다이다
맵의 각 칸은 (A,B) 로 나타낼 수 있다
A 는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.

캐릭터가 움직일 수 있는 방법
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반 시계 방향으로 90도 회전한 방향) 부터 차례대로 갈곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재하면, 왼쪽 방향으로 회전한 다음, 왼쪽으로 한칸 전진한다
    왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 4 방향 모두 가본 칸이거나 바다로 되어있는 칸인 경우, 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다.
    단 . 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우 움직임을 멈춘다.

입력조건)
첫째 줄에 맵의 세로크기 N 과 가로크기 M 을 입력
둘째 줄에 게임 캐릭터의 좌표 (A,B) 와 바라보는 방향 d가 각각 서로 공백으로 구분
0 , 1, 2, 3
북, 동, 남, 서
셋째줄부터 맵의 육지/바다 주어짐 ( 0-육지 // 1- 바다
'''
n,m=map(int,input().split())
d=[[0]*m for _ in range(n)]

x,y,direction=map(int,input().split())
d[x][y]=1

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

count=1
turn_time=0
while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    if d[nx][ny]==0 and array[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1

    if turn_time==4:
        nx=x-dx[direction]
        ny=y-dy[direction]
        if array[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_time=0