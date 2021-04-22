import re
def solution(dartResult):
    dart=re.compile('(\d+)([SDT])([#*]?)').findall(dartResult)
    bonus = { 'S':1, 'D':2,'T':3}
    option = {'':1, '*': 2, '#':-1}

    for i in range(len(dart)):
        if dart[i][2]=='*' :
            dart[i-1]*=2
        dart[i]=int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    print(dart)
    answer=sum(dart)
    return answer
dartResult='1S*2D#3T'
print(solution(dartResult))



