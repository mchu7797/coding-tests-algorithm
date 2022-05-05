N, M = map(int, input().split())
point_cards = []
money_needs = 0

for _ in range(M):
    point_cards.append(list(map(int, input().split())))

point_cards.sort(key = lambda x: -x[0])

for i in range(M - 1):
    if point_cards[i][0] >= N:
        continue
    money_needs += N - point_cards[i][0]

print(money_needs)