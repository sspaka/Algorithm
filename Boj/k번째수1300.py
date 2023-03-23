# k번째 수

# number보다 작거나 같은 원소의 갯수를 구하는 함수
def count_less(number):
    cnt = 0
    # 각 행에서 number보다 작은 원소의 갯수를 구하는 식 min(number//row, n)
    for row in range(1, n+1):
        cnt += min(number//row, n)
    return cnt

n = int(input())
k = int(input())

start = 1
end = n**2
while start <= end:
    mid = (start+end)//2
    # cnt = mid 값보다 같거나 작은 원소들의 갯수
    cnt = count_less(mid)
    print(start, end, mid, cnt)
    if cnt >= k:
        end = mid-1
    else:
        start = mid+1
print(start, end, mid, cnt)
print(start)
