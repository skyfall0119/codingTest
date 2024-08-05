def solution(land):
    

    from collections import deque

    ## 체크한 오일을 한 숫자로 묶음.
    ## 1 은 방문하지 않은 oil.
    ## 2 ~~ 방문해서 오일카운트됨.
    ## -1 스택에 넣은 것들은 -1 (방문 표시. 스택에 중복해서 들어가지 않도록)
    curOilNum = 2
    ## 각 오일별 크기
    oilSizes = {}
    oilSizes[0] = 0
    # 찾은 석유 열
    oilEachCol = {}
    oilSize = 0
    maxOil = 0


    ## bfs 
    for startCol in range(len(land[0])) :

        # 찾은 석유 열
        # 컬럼 딕셔너리 + 세트
        oilEachCol[startCol] = set()
        
        for startRow in range(len(land)) :
            ## 만약 방문안했었고 석유가 있으면
            if land[startRow][startCol] == 1:
                land[startRow][startCol] = -1
                queue = deque([(startRow,startCol)])
                
                ## 시작점부터 dfs 체크
                while queue :
                    row, col = queue.popleft()
                    land[row][col] = curOilNum ##  오일구분넘버로 방문체크
                    oilSize+=1
                    ## 동서남북 연결 확인
                    # 북
                    if (row-1 >= 0) :
                        if land[row-1][col] == 1:
                            land[row-1][col] = -1
                            queue.append((row-1,col))
                    # 남
                    if (row+1 < len(land)) :
                        if land[row+1][col] == 1:
                            land[row+1][col] = -1
                            queue.append((row+1,col))
                    # 서
                    if (col+1 < len(land[0])) :
                        if land[row][col+1] == 1:
                            land[row][col+1] = -1
                            queue.append((row,col+1))
                    # 동
                    if (col-1 >= 0) :
                        if land[row][col-1] == 1:
                            land[row][col-1] = -1
                            queue.append((row,col-1))
                # endWhile

                ## 오일구분넘버 증가
                oilSizes[curOilNum] = oilSize
                oilSize = 0
                curOilNum += 1

            #endIf

            ##  현재 포인트가 0이 아닐경우. (방문했었음. 찾은 석유 열에 추가)
            if land[startRow][startCol] != 0:
                oilEachCol[startCol].add(land[startRow][startCol] )
        #endFor
        
        ## max 보다 현재열 석유가 더 높으면 max 교체
        cnt = 0
        for num in oilEachCol[startCol] :
            cnt += oilSizes[num]
        if maxOil < cnt :
            maxOil = cnt


    #endFor          

    answer = maxOil
    
    return answer