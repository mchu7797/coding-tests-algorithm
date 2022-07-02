import sys

n = int(sys.stdin.readline())
humans = list(map(int, sys.stdin.readline().split()))

humans.sort()

i = 0
j = 0

for k in humans:
    i += k
    j += i

print(j)