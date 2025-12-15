def solution(jobs:list) :
    
    curTime = 0
    totalWaitTime = 0
    numJobs = len(jobs)

    #초기 정렬 
    jobs.sort(key=lambda x: x[0], reverse=True)

    while jobs :
        
        # 시간 업데이트. 현재 시간에 작업 없으면 쭉 땡김.
        if curTime < jobs[-1][0] :
            curTime = jobs[-1][0]
            
        ## 현재 시간 기준 처리할수 있는 작업 체크
        ## 작업들 중 제일 짧은 작업 찾기
        shortTime = float('inf')
        jobInd = -1
        for i in range(len(jobs)-1, -1,-1) :    
            if jobs[i][0] > curTime :
                break
            if shortTime > jobs[i][1]:
                shortTime = jobs[i][1]
                jobInd = i

        # 가장 짧은 작업 pop.
        # 작업에 대한 시간 처리.
        processed = jobs.pop(jobInd)
        curTime += processed[1]
        totalWaitTime += curTime - processed[0]
    
    return totalWaitTime // numJobs
    