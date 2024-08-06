def solution(record):
    answer = []
    idNick = {}
    msg = []
    
    for i in (x.split() for x in record) :
        # unpack
        if len(i) == 3 :
            stat, uid, nick = i
        else :
            stat, uid = i
            
        ## 상태별로 업데이트
        if stat == "Change" :
            idNick[uid] = nick 
        elif stat == "Enter" :
            idNick[uid] = nick 
            msg.append([uid, "님이 들어왔습니다."])
        elif stat == "Leave" :
            msg.append([uid, "님이 나갔습니다."])

    ## 메세지 닉네임 업데이트
    for i in msg :
        answer.append(f"{idNick[i[0]]}{i[1]}")
    
    return answer