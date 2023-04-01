import string


def solution(new_id):
    answer = ''
    answer2 = ''
    possible = list(string.ascii_lowercase)
    possible.extend(['-', '_', '.'])
    for i in range(0, 10):
        possible.append(str(i))
    # 1
    new_id = new_id.lower()
    # 2
    for id in new_id:
        if id in possible: answer += id
    # 3
    flag = False
    for a in answer:
        if not flag:
            if a == '.':
                flag = True
            answer2 += a
        else:
            if a == '.':
                continue
            else:
                answer2 += a
                flag = False
    # 4
    answer2 = list(answer2)
    if answer2 != [] and answer2[0] == '.':
        answer2.pop(0)
    if answer2 != [] and answer2[-1] == '.':
        answer2.pop(-1)

    # 5
    if answer2 == []: answer2.append('a')

    # 6
    if len(answer2) >= 16:
        answer2 = answer2[0:15]
        if answer2[-1] == '.': answer2.pop(-1)
    # 7
    if len(answer2) <= 2:
        answer2.append(answer2[-1])
    if len(answer2) <= 2:
        answer2.append(answer2[-1])

    answer2 = ''.join(answer2)
    return answer2