# 배열의 크기 입력
N, M = map(int, input().split())
arr = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(1, M+1):
        arr[i][j] = temp[j-1]

# 부분의 개수 입력
K = int(input())

for _ in range(K):
    # (i, j) 에서 (x, y)
    i, j, x, y = map(int, input().split())
    result = 0

    # 계산
    for u in range(i, x+1):
        for w in range(j, y+1):
            result += arr[u][w]

    print(result)