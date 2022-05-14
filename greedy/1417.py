n = int(input())
candidate = []

for _ in range(n):
    candidate.append(int(input()))

result = 0

while True:
    biggest = 0
    for i in range(n):
        if candidate[biggest] <= candidate[i]:
            biggest = i
    if biggest == 0:
        break
    candidate[0] += 1
    candidate[biggest] -= 1
    result += 1

print(result)