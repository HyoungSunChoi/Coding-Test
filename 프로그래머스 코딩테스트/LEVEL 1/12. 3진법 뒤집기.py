'''def solution(n):
    res = ''
    while n // 3 >= 1:
        res += str(n % 3)
        n = n // 3
    res += str(n)
    # res 역순 뒤집기
    res=list(map(int,res))
    res=res[::-1]
    print(res)
    answer = 0
    for i in range(len(res)):
        answer+=res[i]*(3**(i))
    return answer
n=125
print(solution(n))'''

def solution(n):
    tmp=''
    while n:
        tmp+=str(n%3)
        n=n//3
    answer= int(tmp,base=10)
    print(answer)
    return answer
solution(45)