import heapq
import copy

k, n = map(int, input().split())
prime = list(map(int, input().split()))
lst = copy.deepcopy(prime)
heapq.heapify(lst)
exist = set() # 중복체크용
i = 0

while i<n:
    # 현재 목록 중에 가장 작은 수를 뽑는다
    now = heapq.heappop(lst)
    # 현재 숫자가 중복이 있는지 확인
    if now in exist:
        continue
    #중복이 없다면 추가하고 i+1
    exist.add(now)
    i += 1
    # 새로 추가 된 수에 대해 가지고 있는 소수들을 곱해서 목록에 추가한다
    for p in prime:
        heapq.heappush(lst, now*p)

print(now)