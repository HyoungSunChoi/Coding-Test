'''import datetime as dt
x=dt.datetime(2016,5,24)-dt.datetime(2016,1,1)
print(x)
def solution(a,b):
    answer=''
    return answer
    144일이 나와야함
'''

def solution(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer=''
    sum=0
    for i in range(a-1):
        sum+=months[i]
    days=b+sum-1
    new_day=days%7
    if new_day==0:
        answer='FRI'
    elif new_day==1:
        answer='SAT'
    elif new_day == 2:
        answer = 'SUN'
    elif new_day == 3:
        answer = 'MON'
    elif new_day == 4:
        answer = 'TUE'
    elif new_day == 5:
        answer = 'WED'
    else:
        answer = 'THU'
    return answer
solution(5,24)