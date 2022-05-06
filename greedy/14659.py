n = int(input())
hills = list(map(int, input().split()))

higher_hill = 0
count = 0
best = 0

for hill in hills:
    if hill > higher_hill:
        higher_hill = hill
        count = 0
    else:
        count += 1
        best = max(best, count)

print(best)