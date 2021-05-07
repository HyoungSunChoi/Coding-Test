n=int(input())
numbers=list(map(int,str(n)))
left=numbers[:len(numbers)//2]
right=numbers[len(numbers)//2:]
if sum(left)==sum(right):
    print("LUCKY")
else:
    print("READY")