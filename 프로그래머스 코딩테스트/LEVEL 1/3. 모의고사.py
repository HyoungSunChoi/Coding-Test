def solution(answers):
    res=[]
    cnt_a=0
    cnt_b = 0
    cnt_c = 0
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for x in range(len(answers)):
        if answers[x]==a[x%len(a)]:
            cnt_a+=1
        elif answers[x]==b[x%len(b)]:
            cnt_b+=1
        elif answers[x]==c[x%len(c)]:
            cnt_c+=1
    answer=[cnt_a,cnt_b,cnt_c]
    for person,score in enumerate(answer):
        if score == max(answer):
            res.append(person+1)
    return res
