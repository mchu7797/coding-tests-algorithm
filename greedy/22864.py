a, b, c, m = map(int, input().split())
fatigue = 0
worked = 0

for _ in range(24):
    if fatigue + a > m:
        if fatigue - c <= 0:
            fatigue = 0
        else:
            fatigue = fatigue - c
    else:
        fatigue = fatigue + a
        worked = worked + b

print(worked)