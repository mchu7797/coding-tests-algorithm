import sys

num_len = int(sys.stdin.readline())
num_arr = []

for _ in range(num_len):
    num = int(sys.stdin.readline())
    num_arr.append(num)

# 산술평균
print(round(sum(num_arr) / num_len))

# 중앙값
num_arr.sort()
print(num_arr[num_len // 2])

# 최빈값
num_freq = [0] * 8000

for i in num_arr:
    num_freq[i + 3999] += 1

freq_max = max(num_freq)

freq_max_indexes = []

for i in range(8000):
    if num_freq[i] == freq_max:
        freq_max_indexes.append(i - 3999)

if len(freq_max_indexes) > 1:
    freq_max_indexes.sort()
    print(freq_max_indexes[1])
else:
    print(freq_max_indexes[0])

# 범위
print(max(num_arr) - min(num_arr))