n = int(input())
v = list(map(int, input().split()))

v.sort(reverse=True)
pay = 0

for i in range(1, n):
    pay += v[i]

print(pay)