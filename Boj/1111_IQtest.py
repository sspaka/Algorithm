# IQ TEST
n = int(input())
x = list(map(int, input().split()))

# n이 1인 경우는 다음에 나올 값을 알 수 없다. 그러므로 'A'
if n == 1:
    print('A')
# n이 2인 경우에는 두가지로 나눠서 생각한다.
# 두 수가 같으면 다음에 나올 수도 같다.
# 두 수가 다르면 a, b 값을 정확히 알 수 없으므로 'A'(알 수 없다)
elif n == 2:
    if x[0] == x[1]:
        print(x[0])
    else:
        print('A')
else:
    if x[0] - x[1] == 0: # zerodivision 에러가 나올 수 있으므로 이런 경우 a = 0이라 해준다.
        a = 0
    else:
        a = (x[1]-x[2])/(x[0]-x[1]) # a와 b는 정수이므로 // 를 사용해준다.
    b = x[1] - a * x[0]
    # 구한 a, b값을 이용하여 값을 구하고 예상과 다른 값이 있다면 'B'출력 후 종료
    for i in range(0, len(x)-1):
        if x[i+1] != x[i]*a + b:
            print('B')
            exit()
    print(x[-1]*a + b) # 마지막 값을 이용하여 닶을 구한다.
