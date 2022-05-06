import math

n = int(input())
prime_order = list(map(int, input().split()))
prime_amount = 0

# 에라토스테네스의 체 구현

prime_list = []
temp = [False, False] + [True] * 999

for i in range(2, 1001):
    if temp[i]:
        prime_list.append(i)
        for j in range(2 * i, 1001, i):
            temp[j] = False

for i in prime_order:
    try:
        prime_list.index(i)
        prime_amount += 1
    except:
        continue

print(prime_amount)