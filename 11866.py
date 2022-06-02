from collections import deque

n, k = map(int, input().split())
queue = deque([x for x in range(1, n + 1)])

print('<', end='')
for _ in range(n - 1):
    for _ in range(k - 1):
        queue.append(queue.popleft())
    print(queue.popleft(), end=', ')
print(queue.popleft(), end='>\n')
