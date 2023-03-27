def dfs(level, left, right):
    global possible, n
    new = abs(left - right)
    if new not in possible:
        possible.append(new)
    if level == n:
        return
    if visit[level][new] == 0:
        dfs(level+1, left+chu[level], right)
        dfs(level+1, left, right + chu[level])
        dfs(level+1, left, right)
        visit[level][new] = 1


n = int(input())
chu = list(map(int, input().split()))
m = int(input())
ball = list(map(int, input().split()))
visit = [[0]*40001 for i in range(n)]


possible = []
dfs(0, 0, 0)

for b in ball:
    if b in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')
