'''
각 자리수의 합 구하기
def sum_digit(number):
    return sum(map(int,str(number)))

def sum_digit(number):
    if number<10:
        return number
    return (number%10)+sum_digit(number//10)

def sum_digit(number):
    add=0
    new=str(number)
    for i in range(len(new)):
        add+=int(new[i])
    return add
'''
# 전체 문자 - 셀프 넘버 아닌 숫자 = 셀프 넘버

def d(n):
    res=n
    for i in list(str(n)):
        res+=int(i)
    return res
lst=[]
for i in range(1,10001):
    lst.append(d(i))
for count in range(1,10000):
    if count in lst:
        continue
    else:
        print(count)


