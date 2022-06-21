import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    h, w, n = map(int, sys.stdin.readline().split())

    for i in range(1, w + 1):
        for j in range(1, h + 1):
            n -= 1
            if n == 0:
                print(j, str(i).zfill(2), sep='')
            