from queue import PriorityQueue

work_count = int(input())

lecture_list = []

for _ in range(work_count):
    lecture_list.append(list(map(int, input().split())))

lecture_list.sort(key=lambda k: (k[2], k[1]))

current_time = 1000000000
min_lecture_room_count = 0
current_lectures = PriorityQueue()

while len(lecture_list) > 0:
    lecture = lecture_list.pop()

    current_time = lecture[2]

    while current_lectures.qsize() > 0:
        current_lecture = current_lectures.get()

        if current_lecture[1] < current_time:
            current_lectures.put(current_lecture)
            break

    current_lectures.put((-lecture[1], lecture[1]))

    if min_lecture_room_count < current_lectures.qsize():
        min_lecture_room_count = current_lectures.qsize()

print(min_lecture_room_count)
