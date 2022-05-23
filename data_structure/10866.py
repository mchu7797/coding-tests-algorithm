from collections import deque
import sys

input_count = int(sys.stdin.readline())
deq = deque()

for _ in range(input_count):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front' and len(command) == 2:
        deq.appendleft(int(command[1]))
    if command[0] == 'push_back' and len(command) == 2:
        deq.append(int(command[1]))
    if command[0] == 'pop_front':
        print(deq.popleft() if deq else -1)
    if command[0] == 'pop_back':
        print(deq.pop() if deq else -1)
    if command[0] == 'size':
        print(len(deq))
    if command[0] == 'empty':
        print(0 if deq else 1)
    if command[0] == 'front':
        print(deq[0] if deq else -1)
    if command[0] == 'back':
        print(deq[-1] if deq else -1)
