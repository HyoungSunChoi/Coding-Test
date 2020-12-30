'''
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

def func(num):

    cnt=0
    while num>0:
        if num>=100:
            lst = []
            for i in list(str(num)):
                lst.append(int(i))
            if (lst[0]+lst[2])//2==lst[1]:
                cnt+=1
                num-=1
        if num<100:
            cnt+=1
            num-=1
    return cnt
'''
def func2(num):
    cnt=0
    for i in range(1,num+1):
        if i<=99:
            cnt+=1
        else:
            nums=list(map(int,str(i)))
            if nums[1]-nums[0]==nums[2]-nums[1]:
                cnt+=1
    return cnt

n=int(input())
print(func2(n))
