# 대표선수
# 우선순위 큐를 사용한다. 최소 힙 가장 작은 값이 루르값.
# heappop을 하면 가장 작은 값이 나온다.
import heapq

n, m = map(int, input().split( ))
score = []
compare = [] # 각 반마다 한명씩 넣어서 비교하는 최소 힙
max_num = 0 # 초기 최대값은 0
answer = 10**9 # 최솟값을 구하므로 초기 값은 최대로 설정
index_list = [1] * n # 인덱스 별로 각 반의 학생 인덱스를 저장한다.

for class_num in range(n):
    data = list(map(int, input().split()))
    data.sort()
    score.append(data)
    # 각 반의 최소점수를 가진 학생부터 반 정보와 함께 최소 힙에 넣는다.
    heapq.heappush(compare, (data[0], class_num))
    max_num = max(max_num, data[0])
print(score)
print(compare)
print(index_list)

while True:
    # 최솟 값을 뺴줍니다.
    minimum = heapq.heappop(compare)
    min_num = minimum[0]
    class_num = minimum[1]
    answer = min(answer, max_num - min_num) # 가장 큰값과 가장 작은 값의 차이를 구하고 answer에 넣는다.
    if index_list[class_num] == m:
        break
    # 나간 학생과 같은 반 학생 중 다음번호 학생을  새롭게 최소 힙에 넣어줍니다.
    heapq.heappush(compare, (score[class_num][index_list[class_num]], class_num))
    # 최소힙에서 가장 큰 값을 구하기 힘드므로, 새로 들어온 학생의 점수가 최대값이 되는지 바로 비교해줍니다.
    max_num = max(max_num, score[class_num][index_list[class_num]])
    index_list[class_num] += 1
    print(compare)
    print(index_list)

print(answer)