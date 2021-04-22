def solution(phone_number):
    res='*'*(len(phone_number)-4)
    return res+phone_number[-4:]

import re
def solution2(num):
    p=re.compile(r'\d(?=\d{4})')
    return p.sub('*',num)
print(solution2('01050381953'))