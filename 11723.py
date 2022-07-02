import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    command_raw = sys.stdin.readline().split()
    command = command_raw[0]
    value = int(command_raw[1]) if len(command_raw) > 1 else 0

    if command == 'add':
        s.add(value)
    elif command == 'remove':
        s.discard(value)
    elif command == 'check':
        print(1 if value in s else 0)
    elif command == 'toggle':
        if value in s:
            s.discard(value)
        else:
            s.add(value)
    elif command == 'all':
        s = set([x for x in range(1, 21)])
    elif command == 'empty':
        s = set()
