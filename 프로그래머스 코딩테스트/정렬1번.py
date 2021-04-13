def solution(num):
    str_list = [int((str(n) * 5)[:5]) for n in num]
    result = ''
    for i in range(len(str_list)):
        idx = str_list.index(max(str_list))
        result += str(num[idx])
        str_list[idx], num[idx] = 0, 0
    return str(int(result))