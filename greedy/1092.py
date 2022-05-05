n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

times = 0

if cranes[0] < boxes[0]:
    print(-1)
    exit()

while len(boxes) > 0:
    for crane in cranes:
        for box in boxes:
            if crane >= box:
                boxes.remove(box)
                break
    times += 1

print(times)