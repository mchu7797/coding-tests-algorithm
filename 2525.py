h, m = map(int, input().split())
time_needs = int(input())

nh, nm = divmod(time_needs, 60)

h += nh
m += nm

if m >= 60:
    h += 1
    m %= 60
if h >= 24:
    h %= 24

print(h, m)