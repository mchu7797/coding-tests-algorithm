dices = list(map(int, input().split()))
dice_same = [0] * 6

for dice in dices:
    dice_same[dice - 1] += 1

for i in range(len(dice_same)):
    if dice_same[i] == 3:
        print(10000 + (i + 1) * 1000)
        exit()
    if dice_same[i] == 2:
        print(1000 + (i + 1) * 100)
        exit()
print(max(dices) * 100)