import math

def is_prime_number(x):
    if x == 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(n, k):
    answer = 0
    result = ''

    while n > k:
        result = str(n % k) + result
        n = n // k
    result = str(n) + result

    result = list(map(str, result.split('0')))
    for r in result:
        if r != '' and is_prime_number(int(r)):
            answer += 1
    return answer