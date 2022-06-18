def check_hansu(i):
    i_str = str(i)    
    if len(i_str) == 1:
        return True
    gap = int(i_str[1]) - int(i_str[0])
    for j in range(2, len(i_str)):
        if gap != int(i_str[j]) - int(i_str[j - 1]):
            return False
    return True

n = int(input())
hansu_count = 0

for i in range(1, n + 1):
    if check_hansu(i):
        hansu_count += 1

print(hansu_count)