n, a, b = map(int, input().split())
subjects = []

for _ in range(10):
    subjects.append(list(map(int, input().split())))

for i in range(10):
    remain_subjects = 6
    for _ in range(subjects[i][0]):
        if a >= 66 or remain_subjects == 0:
            break
        a += 3
        b += 3
        remain_subjects -= 1
    for _ in range(subjects[i][1]):
        if remain_subjects == 0:
            break
        b += 3
        remain_subjects -= 1
    if a >= 66 and b >= 130 and i + n <= 7:
        print("Nice")
        exit()

print("Nae ga wae")