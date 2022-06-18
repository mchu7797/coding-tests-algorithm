t = int(input())
result = []

for _ in range(t):
    a, b = map(int, input().split())
    result.append(a + b)

for i, j in enumerate(result):
    print('Case #{}: {}'.format(i + 1, j))