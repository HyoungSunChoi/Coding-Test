def solution(absolutes, signs):
    answer=0
    for x in range(len(signs)):
        if signs[x]:
            answer+=absolutes[x]*1
        else:
            answer+=absolutes[x]*(-1)

    return answer
absolutes=[4,7,12]
signs=[True,False,True]
print(solution(absolutes,signs))