'''
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.

S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
'''

# 테스트케이스 개수 입력
T=int(input())
# 반복횟수 R, 문자열 S 입력
for _ in range(T):
    # 방법 1, 파이썬 다운 입력받기 <- 이렇게 하자
    case_list=input().split()
    repeat_num=int(case_list[0])
    repeat_string=case_list[1]
    for i in range(len(repeat_string)):
        print(repeat_string[i]*repeat_num,end='')
    print()

    # 방법 2 map 함수사용
    r, s = map(str, input().split())
    r = int(r)
    new_word=[]
    for i in list(map(str,s)):
        new_word+=i*r
    for i in new_word:
        print(i,end='')
    print()
'''
ABC
012
for i in word:
    new_word+=i*r
'''
