def d(i):
    return i + sum(map(int, str(i)))

all_number = []

for i in range(1, 10001):
    all_number.append(d(i))

all_number = list(set(all_number))

for i in range(1, 10001):
    if i not in all_number:
        print(i)