N = int(input())
stairs = [0]

for i in range(1, N + 1):
    stairs.append(int(input()))

option = [0, 0]
record = [0, 0, 0]
current = 0

i = 0
while i < len(stairs):
    