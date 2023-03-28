# 중량제한

from collections import deque

# 중량이 c일때 출발지점에서 목적지점까지 도달할 수 있는지 확인
def bfs(c):
    q = deque()
    q.append(start_node)
    visited = [False] * (n+1) # 방문한 노드 표시하기 위한 리스트
    visited[start_node] = True # 시작 노드 방문 표시.

    while q:
        x = q.popleft()
        for y, weight in graph[x]:
            # 방문한 적이 없는 노드 인지 확인
            # 중량 c가 제한 중량(weight)보다 작은지 확인
            if not visited[y] and weight >= c:
                visited[y] = True
                q.append(y)
    return visited[end_node]


n, m = map(int, input().split())
# n+1길이의 배열 생성
graph = [[] for _ in range(n+1) ]
# 중량의 최대 최소값 설정
Max = 1
Min = 1000000000

# 주어진 값 받기
# x, y, weight = 노드x, 노드y, 간선의 중량 제한
for _ in range(m):
    x, y, weight = map(int, input().split())
    graph[x].append((y, weight))
    graph[y].append((x, weight))
    # 주어진 다리의 제한 중량 중 최대 최소 찾기
    Max = max(Max, weight)
    Min = min(Min, weight)
# 시작 노드, 도착 노드
start_node, end_node = map(int, input().split())

result = Min
while (Min <= Max):
    mid = (Min + Max) // 2
    if bfs(mid):  # 이동이 가능하므로, 중량을 증가 시킵니다.
        result = mid
        Min = mid + 1
    else:  # 이동이 불가능하므로, 중량을 감소시킵니다.
        Max = mid - 1
print(result)
