def solution(a, b):
    day_list = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    cur_day = 5
    answer = ''
    
    num_days={
        1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
    }
    
    days = 0
    for i in range(1, a):
        days += num_days[i]
    days += b
    offset = days % 7 
    
    ind = (cur_day + offset -1) % 7
    
    
    return day_list[ind]