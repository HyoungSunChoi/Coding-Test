'''
행복 왕국의 왕실 정원은 체스판과 같은 8 X 8 좌표 평면이다.
왕실 정원의 특정한 한 칸에 나이트가  서 있다.
나이트는 L 자 형태로만 이동할 수 있다.
1. 수평으로 두칸 이동한 후 수직으로 한칸 이동하기
2. 수직으로 두칸 이동한 후 수평으로 한 칸 이동하기

행 위치는 1~8
열 위치는 a~h


풀이과정)
ord('a','h') = 97 ~ 104
이동 가능 과정
왼쪽 2칸 위/아래 1칸
오른쪽 2칸 위/아래 1칸
아래 2칸 좌/우 1칸
위 2칸 좌/우 1카

총 8가지
'''
steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
p=input()
row=int(p[1])
column=int(ord(p[0])-int(ord('a')))+1
result=0
for step in steps:
    next_row=row+step[0]
    next_column=column+step[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1
print(result)