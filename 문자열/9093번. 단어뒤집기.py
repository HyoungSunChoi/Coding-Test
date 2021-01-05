import sys
n=int(sys.stdin.readline())
word=list(sys.stdin.readline().split() for i in range(n))
for i in range(n):
    for j in word[i]:
        j=j[::-1]
        print(j, end=' ')
    print()