def solution(enroll, referral, seller, amount):

        ## referral dic
    dic_ref = {e:r for e, r in zip(enroll, referral)}

    # dic profit init
    dic_profit = {i:0 for i in enroll}

    def calcProfit(name, made) :
        if name == "-" : # 재귀 끝 
            return 
        fee = int(made*0.1)
        # 내가 번거 90%.
        dic_profit[name] += made - fee 
        
        # 10퍼 상납
        if fee > 0 :
            calcProfit(dic_ref[name], fee)

    # sales update
    for s, a in zip(seller, amount) :            
        calcProfit(s, a*100)

    
    return list(dic_profit.values())
