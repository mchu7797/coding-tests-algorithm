import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    _, m = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))
    queue = []
    turn = 1

    for i, v in enumerate(priority):
        queue.append([i, v])
    while len(queue) > 0:
        dequeue_flag = True
        data = queue.pop(0)
        for i in queue:
            if data[1] < i[1]:
                queue.append(data)
                dequeue_flag = False
                break
        if dequeue_flag:
            if data[0] == m:
                print(turn)
                break
            else:
                turn += 1
