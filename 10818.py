_ = input()
n = list(map(int, input().split()))

min = n[0]
max = n[0]

for i in n:
    if min > i:
        min = i
    if max < i:
        max = i

print(min, max)