import sys

n, m, b = map(int, sys.stdin.readline().split())
earth = []
floor = 0
result = sys.maxsize

for _ in range(n):
    earth += map(int, sys.stdin.readline().split())

for target in range(257):
    min_target = 0
    max_target = 0

    for i in earth:
        if i >= target:
            max_target += i - target
        else:
            min_target += target - i

    if max_target + b >= min_target:
        if min_target + (max_target * 2) <= result:
            result = min_target + (max_target * 2)
            floor = target

print(result, floor)