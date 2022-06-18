n = input()
n_new = n
cycle = 1

if len(n) == 1:
    n += '0'
    n_new += '0'

while True:
    temp = str(int(n_new[0]) + int(n_new[1]))
    n_new = n_new[1] + (temp[1] if len(temp) > 1 else temp[0])
    if n == n_new:
        break
    else:
        cycle += 1
print(cycle)