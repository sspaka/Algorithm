# 위, 아래, 오른쪽, 왼쪽에 붙어 앉아있는 경우
def check1(place):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for row in range(5):
        for col in range(5):
            if place[row][col] == 'P':
                for i in range(4):
                    new_row, new_col = row + dx[i], col + dy[i]
                    if 0 <= new_row <= 4 and 0 <= new_col <= 4 and place[new_row][new_col] == 'P':
                        return True
    return False


# 대각선에 앉아있는데 파티션이 없는 경우
def check2(place):
    dx = [-1, -1, 1, 1]
    dy = [1, -1, 1, -1]
    for row in range(5):
        for col in range(5):
            if place[row][col] == 'P':
                for i in range(4):
                    new_row, new_col = row + dx[i], col + dy[i]
                    if 0 <= new_row <= 4 and 0 <= new_col <= 4 and place[new_row][new_col] == 'P':
                        if place[new_row - dx[i]][new_col] == 'O' or place[new_row][new_col - dy[i]] == 'O':
                            return True
    return False


# 위, 아래, 오른쪽, 왼쪽으로 2칸 떨어져있는데 파티션이 없는 경우
def check3(place):
    dx = [-2, 2, 0, 0]
    dy = [0, 0, -2, 2]
    for row in range(5):
        for col in range(5):
            if place[row][col] == 'P':
                for i in range(4):
                    new_row, new_col = row + dx[i], col + dy[i]
                    if 0 <= new_row <= 4 and 0 <= new_col <= 4 and place[new_row][new_col] == 'P':
                        if place[new_row - (dx[i] // 2)][new_col - (dy[i] // 2)] == 'O':
                            return True
    return False


def solution(places):
    answer = []
    for place in places:  # 세가지 경우에 해당하면 0, 해당사항 없으면 1 추가.
        if check1(place):
            answer.append(0)
        elif check2(place):
            answer.append(0)
        elif check3(place):
            answer.append(0)
        else:
            answer.append(1)
    return answer