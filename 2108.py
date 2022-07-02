from collections import Counter

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

# 산술평균
print(round(sum(nums) / n))

# 중앙값
nums.sort()
print(nums[n // 2])

# 최빈값
nums_counter = Counter(nums)
nums_common = nums_counter.most_common(2)
if len(nums_common) == 2 and nums_common[0][1] == nums_common[1][1]:
    print(nums_common[1][0])
else:
    print(nums_common[0][0])

# 범위
print(nums[-1] - nums[0])