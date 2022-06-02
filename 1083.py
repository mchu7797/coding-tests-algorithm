n = int(input())
a = list(map(int, input().split()))
s = int(input())

for i in range(n):
    max_index = i
    for j in range(i, min(i + s + 1, n)):
        if a[max_index] < a[j]:
            max_index = j
    for j in range(max_index, i, -1):
        temp = a[j]
        a[j] = a[j - 1]
        a[j - 1] = temp
        s -= 1

print(*a)