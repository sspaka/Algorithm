def solution(lottos, win_nums):
    correct = 0
    zero_cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
        if lotto == 0:
            zero_cnt += 1
    answer = [7-(correct+zero_cnt), 7 - correct]
    if answer[0] == 7: answer[0] = 6
    if correct <= 1:
        answer[1] = 6
    return answer