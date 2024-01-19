import sys

def round_v2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

opinion_count = int(sys.stdin.readline())

if opinion_count == 0:
    print(0)
    exit()

start_index = round_v2(opinion_count * (3 / 20))
end_index = opinion_count - round_v2(opinion_count * (3 / 20))

opinion_list = []

for _ in range(opinion_count):
    opinion_list.append(int(sys.stdin.readline()))

opinion_list.sort()

opinion_average = 0

for i in range(start_index, end_index):
    opinion_average += opinion_list[i]

opinion_average /= (end_index - start_index)
opinion_average = round_v2(opinion_average)

print(opinion_average)
