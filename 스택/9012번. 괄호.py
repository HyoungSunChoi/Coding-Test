import sys
n=int(sys.stdin.readline())
for _ in range(n):
    lst=list(sys.stdin.readline())
    while lst!=[]:
        if lst[0]==')':
            print("NO")
            break
        elif lst[0]=='\n':
            lst.pop()
            break
        else:
            if ')' in lst:
                lst.remove(')')
                lst.remove('(')
            else:
                print("NO")
                break
    if lst ==[]:
        print("YES")