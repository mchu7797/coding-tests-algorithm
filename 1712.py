a, b, c = map(int, input().split())

if c - b <= 0:
    print(-1)
    exit()


sale_notebook = 0

if a != 0:
    sale_notebook = a // (c - b) + 1
else:
    sale_notebook = 1
    

print(sale_notebook)