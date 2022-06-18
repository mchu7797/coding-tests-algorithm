max = 0
max_index = 1

for i in range(1, 10):
    num = int(input())
    if max < num:
        max = num
        max_index = i

print(max)
print(max_index)