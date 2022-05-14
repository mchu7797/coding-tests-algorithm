s = input()
zero_to_one = 0
one_to_zero = 0

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i] == '0':
            zero_to_one += 1
        else:
            one_to_zero += 1
if s[len(s) - 1] == '0':
    zero_to_one += 1
else:
    one_to_zero += 1

print(min(zero_to_one, one_to_zero))