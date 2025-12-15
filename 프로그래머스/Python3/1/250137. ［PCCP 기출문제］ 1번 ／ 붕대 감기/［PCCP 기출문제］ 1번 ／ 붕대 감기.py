def solution(bandage, health, attacks):

    cur = 0
    curHealth = health
    
    ## 각 공격시
    for t, dmg in attacks :
        
        ## 붕대 체력회복
        recoveryTime = t - cur -1
        recovAdd = int(recoveryTime / bandage[0]) * bandage[2]
        recovSec = recoveryTime * bandage[1]
        cur = t
        
        curHealth += recovAdd + recovSec
        if curHealth > health :
            curHealth = health
        
        ## 체력업데이트
        curHealth -= dmg
        
        ## 체력 다 소진
        if curHealth <= 0 :
            return -1
        
    ## 남은체력
    return curHealth
