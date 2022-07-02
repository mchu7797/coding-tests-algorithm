import sys

n, m = map(int, sys.stdin.readline().split())
pokemon_dict_stn = {}
pokemon_dict_nts = {}


for i in range(1, n + 1):
    pokemon_name = sys.stdin.readline().split('\n')[0]
    pokemon_dict_nts[i] = pokemon_name
    pokemon_dict_stn[pokemon_name] = i

for i in range(m):
    input_data = sys.stdin.readline().split('\n')[0]

    if input_data.isnumeric():
        print(pokemon_dict_nts[int(input_data)])
    else:
        print(pokemon_dict_stn[input_data])