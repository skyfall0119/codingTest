from collections import deque

def solution(n, info):
    
    answer = [-1]
    ## Bfs
    q = deque()
    # initial : (n, hist)
    q.append((n, [] ))
    diff = -1
    while q :
        left, shotlist= q.popleft()
        ind = len(shotlist)
            
            
        # 0점 인덱스.
        if ind == 10:
            # 남은거 다 0점에 짬
            shotlist.append(left)
            
            ## calculate scores
            ryanWinBy = 0
            for i in range(11) :
                ## 라이언이 이기는 점수
                if shotlist[i] > info[i] :
                    ryanWinBy += 10-i
                ## 라이언이 짐.
                elif info[i] > 0 :
                    ryanWinBy -= 10-i
            
            ## 같은 점수.
            if ryanWinBy == 0 :
                continue
                
            # 더 큰 점수차
            elif ryanWinBy > diff :
                diff = ryanWinBy
                answer = shotlist
            ## 같은 점수차
            elif ryanWinBy == diff :

                ## 낮은거 많이 맞춘거로 업데이트
                for i in range(len(shotlist)-1,-1,-1) :
                    if diff == -1 :  ## 
                        return [-1]
                    elif shotlist[i] > answer[i] :
                        answer = shotlist
                        break
                    elif shotlist[i] < answer[i] : 
                        break
        

        
        ## 10~1점
        else :
            winlist = shotlist.copy()
            loselist = shotlist.copy()
            
            if left > info[ind] :  ## 점수 딸수 있음.
                winlist.append(info[ind]+1)
                q.append((left-(info[ind]+1), winlist))
            
            # lose, left=0 
            loselist.append(0)
            q.append((left, loselist))
            
    ## end of q
                    
    return answer
    