# 백준 13458 시험감독

n = int(input())
A = list(map(int, input().split(' ')))
B, C = map(int, input().split(' '))
answer = n

for idx in range(len(A)):
    if A[idx] > B:
        A[idx] -= B
    else:
        A[idx] = 0

for idx in range(len(A)):
    if A[idx] > 0:
        answer += A[idx] // C
        if A[idx] % C != 0: answer += 1
print(answer)