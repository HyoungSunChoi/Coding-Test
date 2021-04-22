def distance(hand,number):
    location= {'1':(0,0), '2':(0,1), '3':(0,2),
               '4':(1,0), '5':(1,1), '6':(1,2),
               '7':(2,0), '8':(2,1), '9':(2,2),
               '*':(3,0), '0':(3,1), '#':(3,2)}
    hand=str(hand)
    number=str(number)
    x_h,y_h = location[hand]
    x_n,y_n = location[number]
    return abs(x_h-x_n)+abs(y_h-y_n)

def solution(numbers,hand):
    answer=''
    l_chk='*'
    r_chk='#'
    for x in numbers:
        if x in [1,4,7]:
            answer+='L'
            l_chk=x
        elif x in [3,6,9]:
            answer+='R'
            r_chk=x
        else:
            l_dis=distance(l_chk,x)
            r_dis=distance(r_chk,x)
            # 거리가 다른 경우 더 가까운 쪽
            if l_dis==r_dis:
                # 거리가 동일하다면
                if hand=='left':
                    answer+="L"
                    l_chk=x
                answer+="R"
                r_chk=x
            elif l_dis>r_dis:
                answer+="R"
                r_chk=x
            elif l_dis<r_dis:
                answer+="L"
                l_chk=x
    return answer
numbers=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand='left'
print(solution(numbers,hand))
