# 백준에서 시간초과당했음.. 다시 풀 필요가 있어 보임

import sys

k, n = map(int, sys.stdin.readline().split())
cables = []

for _ in range(k):
    cables.append(int(sys.stdin.readline()))

length = 0

for i in cables:
    length += i
length = length // n

while True:
    cable_count = 0
    for i in cables:
        cable_count += (i // length)
    if cable_count >= n:
        print(length)
        break
    else:
        length -= 1