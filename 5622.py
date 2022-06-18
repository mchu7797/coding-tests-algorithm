word = input()
dial_time = 0

for i in word:
    char = ord(i) % 65

    if char < 3:
        dial_time += 3
    elif char < 6:
        dial_time += 4
    elif char < 9:
        dial_time += 5
    elif char < 12:
        dial_time += 6
    elif char < 15:
        dial_time += 7
    elif char < 19:
        dial_time += 8
    elif char < 22:
        dial_time += 9
    elif char < 26:
        dial_time += 10
    else:
        continue

print(dial_time)