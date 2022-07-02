import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
result = 0

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)

for coin in coins:
    while k >= coin:
        result += 1
        k -= coin

print(result)