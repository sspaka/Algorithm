#귀여운 라이언

n, k  = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
ryan = []
answer = n

for i in range(n):
    if lst[i] == 1:
        cnt += 1
        ryan.append(i)
        if cnt >= k:
            answer = min(answer, ryan[-1]-ryan[-1*k])
if cnt < k:
    print(-1)
else:
    print(answer+1)