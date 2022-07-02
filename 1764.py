import sys

n, m = map(int, sys.stdin.readline().split())

deut = {}
deutbo = []

for i in range(n):
    name = sys.stdin.readline().split('\n')[0]
    deut[name] = True

for i in range(m):
    name = sys.stdin.readline().split('\n')[0]
    if name in deut:
        deutbo.append(name)

deutbo.sort()

print(len(deutbo))
for name in deutbo:
    print(name)