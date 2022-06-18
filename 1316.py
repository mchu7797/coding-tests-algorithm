n = int(input())
group_strings = 0

for _ in range(n):
    is_group_string = True
    string = input()
    alphabet = [0] * 26
    before_char = ord(string[0]) % 97

    for i in range(len(string)):
        char = ord(string[i]) % 97
        if alphabet[char] > 0 and before_char != char:
            is_group_string = False
            break
        else:
            alphabet[char] += 1
            before_char = char
    if is_group_string:
        group_strings += 1

print(group_strings)