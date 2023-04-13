path=[]
cnt = {}

def abc(level, start, lst, course_length):
    global path, cnt
    if level==course_length:
        res = ''.join(path[:])
        if res not in cnt: cnt[res] = 1
        else: cnt[res] += 1
        return
    for i in range(start,len(lst)):
        path.append(lst[i])
        abc(level+1,i+1,lst,course_length)
        path.pop(-1)


def solution(orders, course):
    global cnt
    answer = []
    # abc(0, 0, orders[0], 3)
    for c in course:
        cnt = {}
        course_cnt = 0
        for order in orders:
            if len(order) < c: continue
            lst = sorted(list(order))
            abc(0, 0, lst, c)
            course_cnt += 1
        if course_cnt >= 2:
            cnt = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
            max_cnt = cnt[0][1]
            if max_cnt < 2: break
            for case in cnt:
                if case[1] == max_cnt:
                    answer.append(case[0])
                else:
                    break
    answer = sorted(answer)
    return answer