def solution(friends, gifts):

    
    status = {}
    jisu = {}
    
    
    for i in gifts :
        sent, received = i.split(" ")
        ## 선물 현황 딕셔너리로
        if (sent,received) not in status :
            status[sent,received] = 1
        else :
            status[sent,received] += 1

        ## 선물지수
        if sent not in jisu :
            jisu[sent] = [0,0]
        if received not in jisu :
            jisu[received] = [0,0]

        jisu[sent][0] += 1
        jisu[received][1] += 1
        
        
        
    maxGift = 0
    
    for sender in friends :
        giftToGet = 0
        for receiver in friends :
            
            if sender not in jisu :
                jisu[sender] = [0,0]
            if receiver not in jisu :
                jisu[receiver] = [0,0]
                
            jisuSent = jisu[sender][0]-jisu[sender][1]
            jisuReceived = jisu[receiver][0]-jisu[receiver][1]

            ## 주고받은 내역 없음. or 같은 수 주고받음. 지수가 더 크면 받을 선물 증가
            if (((sender, receiver) not in status) and ((receiver, sender) not in status))  :
                if jisuSent - jisuReceived  > 0 :
                    giftToGet += 1

            ## 받은거 없이 주기만 함
            elif (receiver, sender) not in status :
                giftToGet += 1

            ## 준거 없이 받기만 함. 패스
            elif (sender, receiver) not in status :
                pass

            ## 선물 더 많이 줬을때
            elif (status[sender,receiver] > status[receiver,sender]) :
                giftToGet += 1

            ## 선물 수가 같을 때
            elif (status[sender,receiver] == status[receiver,sender]) :
                if jisuSent - jisuReceived > 0 :
                    giftToGet += 1

        # 최고 선물받는 수 업데이트
        if giftToGet > maxGift :
            maxGift = giftToGet

    return maxGift