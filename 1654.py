K, N = map(int, input().split())
cables = []

for _ in range(K):
    cables.append(int(input()))

start, end = 1, max(cables)

while start <= end:
    mid = (start + end) // 2
    cable_count = 0

    for cable in cables:
        cable_count += cable // mid
    
    if cable_count >= N:
        start = mid + 1
    if cable_count < N:
        end = mid - 1
print(end)