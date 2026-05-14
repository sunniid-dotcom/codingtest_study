
#유연근무제 
#2025 프로그래머스 코드챌린지 1차 예선

def solution(schedule, timelogs, startday):
    answer = 0

    for i in range(len(schedule)):
        limit_time = convert(schedule[i]) + 10
        timelog = timelogs[i]
        cur_day = startday - 1

        for log in timelog:
            cur_day += 1

            if cur_day % 7 in [0, 6]:
                continue

            if convert(log) > limit_time:
                break
        else:
            answer += 1

    return answer

def convert(time):
    time = str(time)
    h, m = time[:-2], time[-2:]
    return int(h) * 60 + int(m)

# def solution(schedule, timelogs, startday):
#     answer = 0

#     for i in range(len(schedule)):
#         schedule = convert(schedule[i]) + 10
#         timelog = timelogs[i]
#         cur_day = startday - 1

#         for log in timelog:
#             cur_day += 1

#             if cur_day % 7 in [0, 6]:
#                 continue
#             if convert(log) > schedule:
#                 break

#         else:
#             answer += 1

#     return answer

# def convert(time):
#     time = str(time)
#     h, m = time[:-2], time[-2:]
#     return int(h) * 60 + int(m)