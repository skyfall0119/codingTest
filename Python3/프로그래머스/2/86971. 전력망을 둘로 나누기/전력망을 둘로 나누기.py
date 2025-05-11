def solution(n, wires):
    
    # dic
    conn = {i:[] for i in range(1,n+1)}    
    for a,b in wires :
        conn[a].append(b)
        conn[b].append(a)
            
    
    def dfs(breaknode: set):
        # startNode ==> just start from 1.
        visited = [False for i in range(n)]
        visited[0] = True
        stack = [1]
        
        # dfs
        while stack :
            curNode = stack.pop()
                    
            for nextNode in conn[curNode] :
                # 안끊어진 노드, 방문안한 노드만 스택에 추가. visit 체크. 
                if not visited[nextNode-1] and breaknode != {curNode, nextNode} :
                    stack.append(nextNode)
                    visited[nextNode-1] = True
        return sum(visited)
    
    
    min = n
    
    for wire in wires :
        one = dfs(set(wire))
        dif = abs(n - 2*one)
        if min > dif :
            min = dif
    
    return min