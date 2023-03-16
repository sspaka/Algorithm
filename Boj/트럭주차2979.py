A, B, C = map(int, input().split())
cars = []
for _ in range(3):
    cars.append(list(map(int, input().split())))
# 시간별 주차된 차량 갯수
time = [0]*100
answer = 0
for car in cars:
    i = car[0]
    while i < car[1]:
        time[i] += 1
        i += 1
# 시간대별 차량수로 값구하기
answer = A*time.count(1) + 2*B*time.count(2) + 3*C*time.count(3)
print(answer)