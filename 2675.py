T = int(input())

for _ in range(T):
    r, s = input().split()
    r = int(r)

    for i in s:
        for _ in range(r):
            print(i, end='')
    print()