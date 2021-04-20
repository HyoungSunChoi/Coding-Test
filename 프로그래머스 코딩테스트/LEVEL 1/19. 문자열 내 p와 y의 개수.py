from collections import Counter
def solution(s):
    s=s.lower()
    a=Counter(s)
    if a['p']==a['y']:
        return True
    elif a['p']!=a['y']:
        return False

def solution2(s):
    return s.lower().count('p')==s.lower().count('y')