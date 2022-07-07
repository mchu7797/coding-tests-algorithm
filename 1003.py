zero = [1, 0, 1]
one = [0, 1, 1]

while len(zero) < 41 and len(one) < 41:
    zero.append(zero[-1] + zero[-2])
    one.append(one[-1] + one[-2])

T = int(input())
for i in range(T):
    case = int(input())
    print(zero[case], one[case])