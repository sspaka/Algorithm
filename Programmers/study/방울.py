from itertools import accumulate

def solution(bell):
    coors_start = {}
    coors_end = {}
    for i, x in enumerate(accumulate([0] + [-1 if b == 1 else 1 for b in bell])):
        if x not in coors_start:
            coors_start[x] = i
        coors_end[x] = i
    return max(coors_end[x] - coors_start[x] for x in coors_end)

# 예시로 [1, 2, 1, 1, 1, 2, 2, 1] 이 주어졌을 때,

# 1을 -1로, 2을 1로 치환합니다. => [-1, 1, -1, -1, -1, 1, 1, -1]

# 누적합을 구합니다. => [0, 0 + -1, 0 + -1 + 1, 0 + -1 + 1 + -1, ...] => [0, -1, 0, -1, -2, -3, -2, -1, -2]

# 이 누적합의 i번재 요소는 1~i번째 방울까지 봤을떄 초록방울이 얼마가 더 많았냐 의미합니다. 예를 들어 i=3일때 누적합[i]는 -1이며 이는 1~3번째 방울까지 봤을때 빨간색이 초록보다 1개 더 많음을 의미합니다.

# 따라서 3번째 방울부터 시작해서 구간을 설정할때 색의 갯수를 맞추려면 끝에 -1을 또 찾아야 합니다. 예를 들어, i=7일때 누적합[i]가 -1이고 이는 곧 bell[3:7]의 구간의 초록/빨간 갯수가 같음을 알 수 있습니다.

# 앞서 말했듯이 색이 같은 경우는 숫자가 같은 양끝이 두 색이 같은 경우입니다. 따라서 누적합에 있는 각 값에 대하 가장 멀리 떨어져있는 길이를 구하면 됩니다. 예를 들어 0이 경우,
# [0, -1, 0, -1, -2, -3, -2, -1, -2] 인 경우이고, i=0, 2 이므로 구간의 길이는 2-0 입니다.
# -1의 경우,
# [0, -1, 0, -1, -2, -3, -2, -1, -2] 인 경우이고, i=1, 7 이므로 구간의 길이는 7-1 입니다. 다른 값도 마찬자기로 계산하면(-2은 최대 4 떨어져있음...), i=1, 7 일때 값이 최대가 됨을 알 수 있습니다.

# 내풀이 <- 실패
def solution(bell):
    answer = 0
    bellCnt = [0] * len(bell)
    bellMinus = [[] for _ in range(len(bell)+1)]
    bellPlus = [[] for _ in range(len(bell)+1)]

    for i in range(len(bell)):
        if bell[i] == 2: bell[i] -= 3
        
        if i == 0:
            bellCnt[i] = bell[i]
        else:
            bellCnt[i] = bellCnt[i-1]+bell[i]
    
    for i in range(len(bellCnt)):
        if bellCnt[i] >= 0:
            bellPlus[bellCnt[i]].append(i)
        else:
            bellMinus[-1*bellCnt[i]].append(i)

    # print(bellCnt)
    # print(bellPlus)
    # print(bellMinus)

    for arr in bellPlus:
        if len(arr) >= 2:
            answer = max(answer, arr[-1] - arr[0])

    for arr in bellMinus:
        if len(arr) >= 2:
            answer = max(answer, arr[-1] - arr[0])

    return answer