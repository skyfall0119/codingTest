def solution(video_len, pos, op_start, op_end, commands):
    
    def str2int(time) :
        min, sec = time.split(":")
        return int(min) * 60 + int(sec)

    checkOp = lambda x : True if op_start <= x < op_end else False

    
    video_len, pos, op_start, op_end, = str2int(video_len), str2int(pos), str2int(op_start), str2int(op_end)


    ## 오프닝 끝으로.
    if checkOp(pos) :
        pos = op_end


    for com in commands :
        if com == "next" :
            pos += 10
            if pos > video_len :
                pos = video_len
        elif com == "prev" :
            pos -= 10
            if pos < 0 : 
                pos = 0
        ## 오프닝 끝까지.
        if checkOp(pos):
            pos = op_end
    
    
    min = pos // 60
    sec = pos % 60

    return f"{min:02d}:{sec:02d}"