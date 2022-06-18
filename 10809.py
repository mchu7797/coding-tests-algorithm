S = input()
alphabet = [-1] * 26

for i, v in enumerate(S):
    ascii_char = ord(v) % 97
    if alphabet[ascii_char] == -1:
        alphabet[ascii_char] = i

print(*alphabet)