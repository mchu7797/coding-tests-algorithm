test_case = int(input())

for _ in range(test_case):
    quiz_result = input()
    score_stack = 1
    score = 0

    for i in quiz_result:
        if i == 'O':
            score += score_stack
            score_stack += 1
        else:
            score_stack = 1
    
    print(score)