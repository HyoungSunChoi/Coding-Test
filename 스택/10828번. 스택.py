import sys
N=int(sys.stdin.readline())
stack_lst=list()

for i in range(N):
    func=list(sys.stdin.readline().split())

    if func[0]=="push":
        stack_lst.append(int(func[1]))
    elif func[0]=="pop":
        if not stack_lst:
            print(-1)
        else:
            print(stack_lst.pop())
    elif func[0]=="top":
        if not stack_lst:
            print(-1)
        else:
            print(stack_lst[-1])
    elif func[0]=="size":
        print(len(stack_lst))
    else:
        if len(stack_lst)==0:
            print(1)
        else:
            print(0)