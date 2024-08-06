def solution(record):
    answer = []
    idNick = {}
    msg = []
    
    
    for i in record :
        if i[0] != "L" :
            stat, uid, nick = i.split(" ")
            idNick[uid] = nick
        else :
            stat, uid = i.split(" ")
            

        if stat == "Enter" :
            msg.append([uid, "님이 들어왔습니다."])
        elif stat == "Leave" :
            msg.append([uid, "님이 나갔습니다."])

    
    for i in msg :
        answer.append(f"{idNick[i[0]]}{i[1]}")
    
    return answer