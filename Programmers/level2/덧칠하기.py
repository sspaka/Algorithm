def solution(n, m, section):
    answer = 0
    # 페인트 칠하는 범위 설정
    right = 0
    # 남아있는 색칠해야하는 부분을 담은 배열 생성
    remain = section
    for num in section:
        if num > right:
            right = num + m - 1
            answer += 1
    return answer