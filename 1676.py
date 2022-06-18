def factorial(i):
    result = 1
    for i in range(i):
        result *= (i + 1)
    return result

n = int(input())
n_f = ''.join(reversed(str(factorial(n))))
zero_len = 0

for i in n_f:
    if i == '0':
        zero_len += 1
    else:
        break
print(zero_len)