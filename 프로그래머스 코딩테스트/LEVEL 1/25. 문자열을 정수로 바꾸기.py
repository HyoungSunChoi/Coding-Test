def solution(s):
    #return int(s)
    result=0
    for idx,number in enumerate(s[::-1]):
        if number=='-':
            result*=-1
        else:
            result+= int(number) *(10**idx)
    return result