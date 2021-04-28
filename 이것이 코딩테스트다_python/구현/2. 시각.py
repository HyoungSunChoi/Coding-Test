'''
정수 N 이 입력되면 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각 중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성
'''
n=int(input())
cnt=0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            res= str(i)+str(j)+str(k)
            if '3' in res:
                cnt+=1
print(cnt)