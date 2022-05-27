N = int(input())

count = 1
temp = True
stack = []
track = []

for _ in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        track.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        track.append('-')
    else:
        temp = False
        break
if temp == False:
    print('NO')
else:
    for tr in track:
        print(tr)