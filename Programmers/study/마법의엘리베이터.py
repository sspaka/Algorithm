# (1)지문 이해 및 풀이 계획
# 뒷자리가 0인 수는 0을 빼도 누르는 버튼수가 같습니다.
# (뒤가 0이면 +-1 버튼을 누를 일이 없으므로 /10버튼을 누르면 결국 같음.)
# 따라서 자리수 단위로 감소하는 재귀로 접근하면 쉽게 해결할 수 있습니다.
# 예를 들어 solution(2554)는 solution(255) + 4 와 solution(256) + 6 둘 중 더 적은쪽일것입니다.
# solution(255) + 4은 -1을 4번 하고 2550을 만든 경우고, solution(256) + 6은 +1을 6번하고 2560을 만든 경우입니다.

def solution(storey):
    if storey <= 1:
        return storey
    q, r = divmod(storey, 10)
    return min(solution(q) + r, solution(q+1) + (10-r) )