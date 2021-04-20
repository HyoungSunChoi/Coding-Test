def solution(s, n):
    answer = ''
    for x in s:
        if x.isupper():
            answer += chr((ord(x) - ord('A') + n) % 26 + ord('A'))
        elif x.islower():
            answer += chr((ord(x) - ord('a') + n) % 26 + ord('a'))
        elif x == ' ':
            answer += ' '

    return answer


s = 'z'
print(solution(s, 1))
