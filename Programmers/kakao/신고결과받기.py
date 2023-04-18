def solution(id_list, report, k):
    record = {}
    cnt = {}
    out = []
    answer = []

    for id in id_list:
        record[id] = []
        cnt[id] = 0
    for r in report:
        a, b = map(str, r.split())
        if b not in record[a]:
            record[a].append(b)
    for value in record.values():
        if value != []:
            for v in value:
                cnt[v] += 1

    for key, value in cnt.items():
        if value >= k:
            out.append(key)

    for value in record.values():
        res = 0
        for o in out:
            if o in value:
                res += 1
        answer.append(res)
    return answer