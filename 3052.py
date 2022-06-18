remainder_usage = [0] * 42

for i in range(10):
    num = int(input())
    remainder_usage[num % 42] += 1

count = 0

for i in remainder_usage:
    if i > 0:
        count += 1

print(count)