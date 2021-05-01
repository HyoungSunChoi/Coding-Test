'''
현재 캐릭터의 점수를 N 이라고 할 때 자릿수 기준 점수 N 을 반으로 나누어 왼쪽 부분의 자릿수의 합, 오른쪽 부분의 자릿수의 합을 더한 값
ex) 123,402  왼쪽 1+2+3 , 오른쪽 4+0+2 // 두 합이 각각 6이므로 럭키 스트레이트 사용 가능
'''
s=input()
left_s = s[:len(s)//2]
right_s = s[len(s)//2:]
left_sum, right_sum=0,0
for i in range(len(s)//2):
    left_sum+=int(left_s[i])
    right_sum+=int(right_s[i])
if left_sum==right_sum:
    print('LUCKY')
else:
    print('READY')