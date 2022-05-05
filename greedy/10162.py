t = int(input())

A = 0
B = 0
C = 0

if t >= 300:
    while t >= 300:
        t = t - 300
        A = A + 1

if t >= 60:
    while t >= 60:
        t = t - 60
        B = B + 1

if t >= 10:
    while t >= 10:
        t = t - 10
        C = C + 1

if t > 0:
    print(-1)
else:
    print(A, B, C)