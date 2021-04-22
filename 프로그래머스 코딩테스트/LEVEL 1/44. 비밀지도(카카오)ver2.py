def solution(n,arr1,arr2):
    answer=[]
    for i,j in zip(arr1,arr2):
        a= str(bin(i|j)[2:])
        a=a.rjust(n,'0')
        a=a.replace('1','#')
        a=a.replace('0',' ')
        answer.append(a)
    return answer

arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
n=5
print(solution(n,arr1,arr2))
print(bin(9|11))
print(bin(9))
print(bin(11))