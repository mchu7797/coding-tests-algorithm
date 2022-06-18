c = int(input())

for i in range(c):
    scores = list(map(int, input().split()))
    student_count = scores.pop(0)
    average = sum(scores) / student_count
    over_average = 0

    for i in scores:
        if i > average:
            over_average += 1
    
    over_average_ratio = over_average / student_count * 100
    print('{:.3f}%'.format(over_average_ratio))