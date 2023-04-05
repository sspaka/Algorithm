def solution(participant, completion):
    cnt = {}
    hashSum = 0 

    for p in participant:
        cnt[hash(p)] = p
        hashSum += hash(p)

    for c in completion:
        hashSum -= hash(c)
    
    return cnt[hashSum]