import sys
n=int(sys.stdin.readline())
res=[]
op=[]
count=1
flg=True
for _ in range(n):
    a=int(sys.stdin.readline())
    while count<=a:
        res.append(count)
        count+=1
        op.append('+')
    if res[-1]==a:
        res.pop()
        op.append('-')
    else:
        flg=False
if flg==False:
    print("NO")
else:
    for _ in op:
        print(_)