import re


def SDT(string):
    if string[-1] == 'S':
        return int(string[:-1])
    elif string[-1] == 'D':
        return int(string[:-1]) ** 2
    elif string[-1] == 'T':
        return int(string[:-1]) ** 3
    else :
        # 아차상인 경우
        return -SDT(string[:-1])

def solution(dartResult):
    scores = re.compile('\d?\d[SDT][*#]?').findall(dartResult)
    result, last = 0, 0
    for score in scores:
        print('나눠진 word', score)
        print(score[-1])
        if score[-1] != '*':
            last=SDT(score)
            result+=last
        else:
            result+= last + SDT(score[:-1])*2
            last = SDT(score[:-1])*2
    return result


print(solution('1S*2D3T'))
