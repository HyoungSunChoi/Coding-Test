from collections import deque
board=	[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
def solution(board,moves):
    moves=deque(moves)
    stack=[]
    stack=deque(stack)
    cnt=0
    while moves:
        tmp=moves.popleft()
        print(tmp)
        for i in range(len(board)):
            if board[i][tmp-1]!=0:
                if stack and stack[-1]==board[i][tmp-1]:
                    cnt+=1
                    board[i][tmp-1]=0
                    stack.pop()
                    break
                else:
                    stack.append(board[i][tmp-1])
                    board[i][tmp-1]=0
                    break
        for x in range(len(board)):
            print(board[x])
        print()
    return cnt*2
print(solution(board,moves))
