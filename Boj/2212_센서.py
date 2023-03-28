k = int(input())
n = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
total = []

if k <= n:
    print(0)
else:
    for i in range(len(sensor) - 1):
        total.append(sensor[i + 1] - sensor[i])
    total.sort()

    for _ in range(n - 1):
        total.pop()

    print(sum(total))
