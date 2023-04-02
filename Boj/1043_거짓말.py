# 거짓말
def isOkay(li):
    for person in li:
        if person in truth:
            return False
    return True

people ,party = map(int, input().split())
truth = list(map(int, input().split()))
if truth[0] == 0:
    print(party)
    exit()
truth = truth[1:]
cnt = 0
whoInParty = []

for _ in range(party):
    whoInParty.append(list(map(int, input().split()))[1:])

for _ in range(party):
    for who in whoInParty:
        if not isOkay(who):
            truth.extend(who)

for who in whoInParty:
    if isOkay(who):
        cnt += 1
print(cnt)