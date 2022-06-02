board_raw = input()
board = []

amount = 0
before = board_raw[0]

for i in board_raw:
    if before != i:
        if before == 'X':
            board.append(amount)
        else:
            board.append(-amount)
        amount = 1
    else:
        amount += 1
    before = i
    
if board_raw[len(board_raw) - 1] == 'X':
    board.append(amount)
else:
    board.append(-amount)

result = ''
    
for b in board:
    if b % 2 != 0 and b > 0:
        print(-1)
        exit()
    
    if b > 0:
        amount_a = b // 4
        amount_b = (b % 4) // 2
        for _ in range(amount_a):
            result += 'AAAA'
        for _ in range(amount_b):
            result += 'BB'
    else:
        for _ in range(-b):
            result += '.'

print(result)
