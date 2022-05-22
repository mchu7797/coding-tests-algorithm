command_count = int(input())
stack = []

for _ in range(command_count):
    command = input().split()
    if command[0] == 'push' and len(command) == 2:
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if stack else 1)
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        print('ERROR!')