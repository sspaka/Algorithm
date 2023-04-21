def solution(numbers, hand):
    answer = ''
    position = [10, 12]
    arr = [[] for _ in range(4)]
    for i in range(1, 13):
        arr[(i - 1) // 3].append(i)

    for number in numbers:
        if number in [1, 4, 7]:
            position[0] = number
            answer += "L"
        elif number in [3, 6, 9]:
            position[1] = number
            answer += "R"
        elif number in [2, 5, 8, 0]:
            if number == 0: number = 11
            y, x = (number - 1) // 3, (number % 3) - 1
            ly, lx = (position[0] - 1) // 3, 2 if (position[0] % 3) == 0 else (position[0] % 3) - 1
            ry, rx = (position[1] - 1) // 3, 2 if (position[1] % 3) == 0 else (position[1] % 3) - 1

            left_distance = abs(ly - y) + abs(lx - x)
            right_distance = abs(ry - y) + abs(rx - x)

            if left_distance < right_distance:
                position[0] = number
                answer += "L"
            elif left_distance > right_distance:
                position[1] = number
                answer += "R"
            else:
                if hand == "left":
                    position[0] = number
                    answer += "L"
                else:
                    position[1] = number
                    answer += "R"
    return answer