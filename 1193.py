x = int(input())
i = 1

while x > i:
    x -= i
    i += 1

if i % 2 == 0:
    print('{}/{}'.format(
        x,
        i - x + 1
    ))
else:
    print('{}/{}'.format(
        i - x + 1,
        x
    ))

