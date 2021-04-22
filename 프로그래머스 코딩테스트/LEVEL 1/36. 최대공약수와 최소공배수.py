def solution(n,m):
    result=[]
    result.append(GCD(n,m))
    result.append(LCM(n,m))
    return result


# 유클리드 호제법 사용
def GCD(a,b):
    while b>0:
        temp=b
        b=a%b
        a=temp
    return a

def LCM(a,b):
    return a*b/GCD(a,b)