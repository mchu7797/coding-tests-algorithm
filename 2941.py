word = input()
croatian_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatian_alphabet:
    word = word.replace(i, '*')

print(len(word))