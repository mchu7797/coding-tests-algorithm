work_count = int(input())

work_list = []

for _ in range(work_count):
    work_list.append(list(map(int, input().split())))

work_list.sort(key=lambda k: (k[1], -k[0]))

end_point = 1000000

while len(work_list) > 0:
    work = work_list.pop()
    
    if end_point > work[1]:
        end_point = work[1]
    
    end_point -= work[0]

if (end_point < 0):
    print(-1)
else:
    print(end_point)
