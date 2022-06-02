n = int(input())
seats = input()

single = 0
couple = 0

for seat in seats:
    if seat == 'S':
        single += 1
    else:
        couple += 1

cupholder_max = single + couple // 2 + 1

print(n if n < cupholder_max else cupholder_max)