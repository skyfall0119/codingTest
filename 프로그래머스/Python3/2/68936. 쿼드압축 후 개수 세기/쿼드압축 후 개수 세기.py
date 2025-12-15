
cnt = [0,0]

def quadCheck(arr) :
    global cnt

    

    ## 제일 마지막 단계까지 왔으면.
    if len(arr) == 1 :
        if arr[0][0] == 0 :
            return True, 0
        else :
            return True, 1
    
    ## 4개 이상이면 분할해서 확인
    divInd = int(len(arr) /2 )
    
    (same1, quad1) = quadCheck([x[:divInd] for x in arr[:divInd]])
    (same2, quad2) = quadCheck([x[divInd:] for x in arr[:divInd]])
    (same3, quad3) = quadCheck([x[:divInd] for x in arr[divInd:]])
    (same4, quad4) = quadCheck([x[divInd:] for x in arr[divInd:]])
    
    ## 4 분면이 다 압축돼서 올라왔을때
    if same1 and same2 and same3 and same4 :
        numOne = quad1 + quad2 + quad3 + quad4
        if numOne == 4 :  ## 1로 압축
            return True, 1  
        elif numOne == 0 :  ## 0으로 압축
            return True, 0
        
     ## 압축 불가능. 0,1 카운트
    if same1 :
        cnt[quad1] +=1
    if same2 :
        cnt[quad2] +=1
    if same3 :
        cnt[quad3] +=1
    if same4 :
        cnt[quad4] +=1
    return False, 0
        
def solution(arr):

    global cnt
    
    (final, val) = quadCheck(arr)
    
    if final :
        cnt[val] +=1
    
    return cnt