def solution(n, computers):
    answer = 0
    
    ## 방문 확인 boolean 추가
    visited = list(map(lambda x:{"network":x, "visited": False}, computers))
    print(visited)
    
    
    
    for checkingCom in visited :
        
        ## 방문 안했던 컴퓨터면 네트워크 +1
        if not checkingCom["visited"] :
            answer += 1
            checkingCom["visited"] = True
        
        ## 같은 네트워크 체크 DFS
        stack = []
        for netInd, connected in enumerate(checkingCom["network"]) :
            # 연결된 컴퓨터 + 아직 방문안한 컴퓨터 스택에 추가
            if connected and not visited[netInd]["visited"] :    
                stack.append(visited[netInd])

        while stack :
                    
                    
            connectedCom = stack.pop()
            connectedCom["visited"] = True
            
            for netInd, connected in enumerate(connectedCom["network"]) :
            # 연결된 컴퓨터 + 아직 방문안한 컴퓨터 스택에 추가
                if connected and not visited[netInd]["visited"] :    
                    stack.append(visited[netInd])

    
    return answer