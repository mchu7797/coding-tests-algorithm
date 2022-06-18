test_case = int(input())

for i in range(test_case):
    x, y = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(
        i + 1, x, y, x + y
    ))