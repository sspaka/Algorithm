from collections import deque

def bfs():
    while q:
        x, y, key, cnt = q.popleft()
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m and maze[new_x][new_y] !='#' and not visited[new_x][new_y][key]:
                if maze[new_x][new_y] == ".":
                    visited[new_x][new_y][key] = 1
                    q.append([new_x, new_y, key, cnt + 1])
                elif maze[new_x][new_y] == "1":
                    return cnt + 1
                else:
                    if maze[new_x][new_y].isupper():
                        if key & 1 << (ord(maze[new_x][new_y]) - 65):
                            visited[new_x][new_y][key] = 1
                            q.append([new_x, new_y, key, cnt + 1])
                    elif maze[new_x][new_y].islower():
                        nc = key | (1 << ord(maze[new_x][new_y]) - 97)
                        if visited[new_x][new_y][nc] == 0:
                            visited[new_x][new_y][nc] = 1
                            q.append([new_x, new_y, nc, cnt + 1])

    return -1

maze = []
n, m = map(int, input().split())

for x in range(n):
    data = list(input())
    if '0' in data:
        y = data.index('0')
        pos = (x, y)
    maze.append(data)

maze[pos[0]][pos[1]] = '.'

# 큐 만들기, 이동 횟수 딕셔너리 만들기
q = deque()
q.append([pos[0], pos[1], 0, 0])

# 왼, 오, 위, 아래,
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[0] * 64 for _ in range(m)] for _ in range(n)]
visited[pos[0]][pos[1]][0] = 1

print(bfs())