prioDics = {
            "diamond" : {'diamond':1,'iron':1,'stone':1}, 
            "iron":{'diamond':5,'iron':1,'stone':1}, 
            "stone":{'diamond':25,'iron':5,'stone':1}
                }


def pickOne(picks, minerals, pickInd) :
    piro = 0
    diaPiro = ironPiro = stonePiro = 1250
    diaPick = picks[0]
    ironPick = picks[1]
    stonePick = picks[2]
    
    
    ## 각 픽마다 미네랄 피로도 계산
    if pickInd == 0 :
        diaPick -= 1
        for mineral in minerals[:5] :
            piro += prioDics["diamond"][mineral]
    elif pickInd == 1 :
        ironPick -= 1
        for mineral in minerals[:5] :
            piro += prioDics["iron"][mineral]
    elif pickInd == 2 :
        stonePick -= 1
        for mineral in minerals[:5] :
            piro += prioDics["stone"][mineral]
            
            
    ## 전체픽이 다 떨어졌거나 미네랄 끝까지 했으면 리턴
    if (len(minerals) == 0)  or (stonePick + ironPick + diaPick == 0) :
        return piro 
    
    ## 그 다음 미네랄 피로도 계산해서 제일 낮은것을 합치기.

    if diaPick != 0 : ## 다이아곡괭이
        diaPiro = pickOne([diaPick, ironPick, stonePick], minerals[5:], 0)
    if ironPick != 0 : ## 철곡괭이
        ironPiro = pickOne([diaPick, ironPick, stonePick], minerals[5:], 1)
    if stonePick != 0 : ## 돌곡괭이
        stonePiro = pickOne([diaPick, ironPick, stonePick], minerals[5:], 2)

    return piro + min(diaPiro, ironPiro, stonePiro)


def solution(picks, minerals):
    ## max piro
    diaPiro = ironPiro = stonePiro = 1250  

    ## 미네랄 피로도 계산해서 제일 낮은것.
    if picks[0] != 0 : ## 다이아곡괭이
        diaPiro = pickOne(picks, minerals, 0)
    if picks[1] != 0 : ## 철곡괭이
        ironPiro = pickOne(picks, minerals, 1)
    if picks[2] != 0 : ## 돌곡괭이
        stonePiro = pickOne(picks, minerals, 2)

    answer = min(diaPiro, ironPiro, stonePiro)
    
    return answer