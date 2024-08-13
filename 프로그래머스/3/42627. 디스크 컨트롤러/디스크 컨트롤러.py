def solution(jobs) :
    
    curTime = 0
    totalWaitTime = 0
    numJobs = len(jobs)

    #초기 정렬 
    jobs.sort(key=lambda x: x[0], reverse=True)

    while jobs :
        
        ## 작업 다 끝났으면 종료
        if len(jobs) == 0 :
            break
        
        # 시간 업데이트. 현재 시간에 작업 없으면 쭉 땡김.
        if curTime < jobs[-1][0] :
            curTime = jobs[-1][0]
            
        ## 현재 시간 기준 처리할수 있는 작업 체크
        ## 작업들 중 제일 짧은 작업 찾기
        shortTime = -1
        jobInd = -1
        for i in range(len(jobs)-1, -1,-1) :    
            if jobs[i][0] > curTime :
                break
            if shortTime == -1 or (shortTime != -1 and shortTime > jobs[i][1]):
                shortTime = jobs[i][1]
                jobInd = i

        # 가장 짧은 작업 pop
        processed = jobs.pop(jobInd)

        print(processed)
        curTime += processed[1]
        totalWaitTime += curTime - processed[0]
    
    return totalWaitTime // numJobs