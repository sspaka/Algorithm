S = list(input())
now = S[0]
answer = 0

for i in range(1, len(S)):
    if S[i] != now:
        answer += 1
    now = S[i]

print((answer+1)//2)