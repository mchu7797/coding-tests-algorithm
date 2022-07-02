import sys

n, m = map(int, sys.stdin.readline().split())
password_dic = {}

for _ in range(n):
    data = sys.stdin.readline().split()
    password_dic[data[0]] = data[1]

for _ in range(m):
    domain = sys.stdin.readline().split('\n')[0]
    if domain in password_dic:
        print(password_dic[domain])
    else:
        print('null')