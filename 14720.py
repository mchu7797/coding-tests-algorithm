N = int(input())
shops = list(map(int, input().split()))

next_milk = 0
drinked_milk = 0

for i in shops:
    if next_milk == i:
        drinked_milk = drinked_milk + 1
        next_milk = next_milk + 1 if next_milk != 2 else 0
    
print(drinked_milk)