import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(trees)

def get_woods(meter):
    woods = 0
    for tree in trees:
        woods += tree - meter if tree > meter else 0
    return woods

while start <= end:
    mid = (start + end) // 2
    woods = get_woods(mid)
    
    if woods >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)