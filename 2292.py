n = int(input())

t = 1
r = 6
nn = 1

while nn < n:
    nn += r * t
    t += 1

print(t)