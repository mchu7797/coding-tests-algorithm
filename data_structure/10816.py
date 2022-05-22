_ = int(input())
n = list(map(int, input().split()))
_ = int(input())
m = list(map(int, input().split()))

n_dic = {}

for i in n:
    if i not in n_dic:
        n_dic[i] = 1
    else:
        n_dic[i] += 1

for i in m:
    print(0 if i not in n_dic else n_dic[i], end=' ')
print()
