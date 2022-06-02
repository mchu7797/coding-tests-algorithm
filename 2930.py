R = int(input())
player = list(input())
N = int(input())
another = []

default_score = 0
max_score = 0

for _ in range(N):
    another.append(list(input()))

def check_rsp(p1, p2):
    if p1 == 'R':
        if p2 == 'R':
            return 1
        elif p2 == 'S':
            return 2
        else:
            return 0
    elif p1 == 'S':
        if p2 == 'R':
            return 0
        elif p2 == 'S':
            return 1
        else:
            return 2
    else:
        if p2 == 'R':
            return 2
        elif p2 == 'S':
            return 0
        else:
            return 1

for i in range(R):
    for j in range(N):
        default_score = default_score + check_rsp(player[i], another[j][i])

for i in range(R):
    scores = [0, 0, 0]
    for j in range(N):
        scores[0] = scores[0] + check_rsp('R', another[j][i])
        scores[1] = scores[1] + check_rsp('S', another[j][i])
        scores[2] = scores[2] + check_rsp('P', another[j][i])
    max_score = max_score + max(scores)

print(default_score, max_score)