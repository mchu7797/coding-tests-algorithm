n = int(input())
arr = list(map(int, input().split()))
s = int(input())

def swap_arr(i):
    temp = arr[i]
    arr[i] = arr[i + 1]
    arr[i + 1] = temp

biggest = [0, 0]

for i in range(n - 1):
    if s == 0:
        break
    if arr[i] < arr[i + 1]:
        swap_arr(i)
        s -= 1

print(''.join(str(x) + ' ' for x in arr))