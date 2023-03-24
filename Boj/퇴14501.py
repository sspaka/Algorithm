# 백준 14501 퇴사
# dp[day] = max(dp[day+1], dp[day+t[day]] + p[day]
INF = float("-inf")


def solve(day):
    if day > n: return INF
    if day == n: return 0

    res = cache[day]
    if res != -1: return res
    res = max(solve(day + 1), solve(day + times[day]) + outputs[day])
    cache[day] = res
    return res

n = int(input())
times = []
outputs = []
cache = [-1]*n


for _ in range(n):
    time, output = map(int, input().split(' '))
    times.append(time)
    outputs.append(output)

print(solve(0))