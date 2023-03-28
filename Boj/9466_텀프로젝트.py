import sys
sys.setrecursionlimit(100001) #충분한 재귀 깊이를 주어 오류를 예방

def dfs(n):
    global team
    visited[n] = True
    history.append(n) # 선택과정을 기록
    next = select[n]-1
    if visited[next]: #방문 가능한 곳이 종료
        if next in history: #팀을 이루는 지 확인
            team += history[history.index(next):] #팀이 이뤄지는 곳 이후부터 저장
        return
    else:
        dfs(next)

T = int(input())
for _ in range(T):
    N = int(input())
    select = list(map(int, input().split()))
    visited = [False] * N
    team = [] # 팀을 이룬 사람 저장

    for i in range(0, N):
        if not visited[i]: #방문 안한 경우만
            history = []
            dfs(i)
    print(N - len(team))