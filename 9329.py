testcase = int(input())
results = []

for _ in range(testcase):
    n, m = map(int, input().split())
    prizes = []
    amout_stickers = []
    earned_rewards = 0

    for _ in range(n):
        prizes.append(list(map(int, input().split())))
    amout_stickers = list(map(int, input().split()))

    prizes.sort(key = lambda x: -x[len(x) - 1])

    for prize in prizes:
        reward = prize[len(prize) - 1]
        need_stickers = prize[1:len(prize) - 1]
        can_get_prize = True
        while can_get_prize:
            for sticker in need_stickers:
                if amout_stickers[sticker - 1] == 0:
                    can_get_prize = False
            if can_get_prize:
                for sticker in need_stickers:
                    amout_stickers[sticker - 1] -= 1
                earned_rewards += reward
    
    results.append(earned_rewards)

for result in results:
    print(result)