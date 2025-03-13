def solution(storage, requests):
    answer = len(storage) * len(storage[0])
    
    width = len(storage[0]) +2
    height = len(storage)+2
    
    # padd with 0 . meaning outside (accessible by forklift)
    storage2 = [["0"] * (len(storage[0])+2)]
    for row in storage :
        storage2.append(["0"]+list(row)+["0"])
    storage2.append(["0"] * (len(storage[0])+2))
    
    
    # Check for a neighboring '0'
    def _nearZero(i, j):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if storage2[i + dx][j + dy] == '0':
                return True
        return False

    
    for req in requests :
        remvList = []
        
        for i in range(1, height-1):
            for j in range(1,width-1):
                
                ## crane
                if len(req) == 2:
                    if storage2[i][j] == req[0]:
                        # if _nearZero(i,j):
                        #     remvList.append((i,j,'0'))
                        # else:
                        remvList.append((i,j,'1'))
                    
                elif len(req) == 1:
                    if storage2[i][j] == req[0] and _nearZero(i,j):
                        remvList.append((i,j,'0'))
        
        
        ## replace container with status code 0 or 1
        for i,j,status in remvList:
            answer -=1
            storage2[i][j] = status
        
    
        # check 1s if they are near 0 (accessible by forklift)
        
        onesNearZeros = True
        while onesNearZeros:
            convList = []
            for i in range(1, height-1):
                for j in range(1,width-1):
                    if storage2[i][j] == "1" and _nearZero(i,j):
                        convList.append((i,j))
            
            if convList:
                for i, j in convList:
                    storage2[i][j] = "0"
            else:
                onesNearZeros = False
                    
        

    return answer