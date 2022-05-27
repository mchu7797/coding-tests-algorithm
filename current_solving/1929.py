def binary_search(arr, value):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            end = mid - 1
        else:
            start = mid + 1

erathos = [0] * 1000001

for i in range(2, 1000001):
    erathos[i] = i

for i in range(2, 1000001):
    if erathos[i] == 0:
        continue
    for j in range(i * 2, 1000001, i):
        erathos[j] = 0

start, end = map(int, input().split())

for i in range(len(erathos)):
    if start <= erathos[i] <= end:
        print(erathos[i])
    if erathos[i] > end:
        break