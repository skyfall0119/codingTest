def solution(schedules, timelogs, startday):
    answer = 0
    def add10min(time):
        if time % 100 + 10 >= 60:
            return time + 110 - 60
        return time + 10
    
    print(add10min(1255))
    
    for i in range(len(schedules)):
        injung_time = add10min(schedules[i])
        reward = True
        for j in range(len(timelogs[i])):
            current_day = (j + startday)%7
            if current_day == 6 or current_day==0:
                continue
                
            if injung_time < timelogs[i][j]  :
                reward = False
                break
        if reward :
            answer += 1
            

    return answer