def solution(survey, choices):
    answer = ''
    lst = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0,
    }

    for i in range(len(survey)):
        if choices[i] < 4:
            lst[survey[i][0]] += (4 - choices[i])
        else:
            lst[survey[i][1]] += (choices[i] - 4)
    # print(lst)
    if lst['R'] >= lst['T']:
        answer += 'R'
    else:
        answer += 'T'
    if lst['C'] >= lst['F']:
        answer += 'C'
    else:
        answer += 'F'
    if lst['J'] >= lst['M']:
        answer += 'J'
    else:
        answer += 'M'
    if lst['A'] >= lst['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer