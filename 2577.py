number_usage = [0] * 10
number = 1

for _ in range(3):
    number *= int(input())

number = str(number)

for i in number:
    number_usage[int(i)] += 1

for i in number_usage:
    print(i)