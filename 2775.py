import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    floor = [i for i in range(1, n + 1)]

    for _ in range(k):
        for i in range(1, n):
            floor[i] += floor[i - 1]
    
    print(floor[-1])