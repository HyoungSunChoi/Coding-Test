numbers=list(map(int,input().split()))
res=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        res.append(numbers[i]+numbers[j])
print(res)
res=set(res)
print(res)
