def solution(n, lost, reserve):
    answer = 0
    n_reserve = [i for i in reserve if i not in lost]
    n_lost = [i for i in lost if i not in reserve]
    n_lost_2 = [i for i in lost if i not in reserve]

    print(n_reserve, n_lost)
    for i in n_reserve:
        if i - 1 in n_lost:
            n_lost.remove(i - 1)
        elif i + 1 in n_lost:
            n_lost.remove(i + 1)

    for i in n_reserve:
        if i + 1 in n_lost_2:
            n_lost_2.remove(i + 1)
        elif i - 1 in n_lost_2:
            n_lost_2.remove(i - 1)

    return max(n - len(n_lost), n - len(n_lost_2))