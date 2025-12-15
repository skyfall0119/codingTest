def solution(info, edges):
    answer = 0
    
    ## curNode, possibleNextNode, sheepCnt, wolfCnt
    startNode = 0
    stack = [[startNode, {0}, 0,0]]
    
    # dfs 
    while stack :
        curNode, nextNode, scnt, wcnt = stack.pop()
        nextNode.remove(curNode)
        # sheep wolf update
        if info[curNode] == 0 :
            scnt += 1
        else :
            wcnt += 1
            
        ## update answer
        answer = max(answer, scnt)
        
        # update nextnode
        if scnt > wcnt :
            newNode = {y for x,y in edges if x == curNode}
            nextNode.update(newNode)
            
        # add possible moves to stack
        for n in nextNode :
            stack.append(
                (n,nextNode.copy(), scnt, wcnt)
            )

        
    
    return answer