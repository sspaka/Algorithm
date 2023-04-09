def solution(numbers):
    answer = ''
    strings = []
    if max(numbers) == 0:
        return '0'

    for i in numbers:
        s = str(i)
        strings.append(s)

    strings = sorted(strings, key=lambda x: x * 4, reverse=True)

    for i in strings:
        answer += i

    return answer