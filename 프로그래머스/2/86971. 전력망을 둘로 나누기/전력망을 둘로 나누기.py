def solution(n, wires):
    
    # dic
    conn = {}
    for a,b in wires :
        if a in conn :
            conn[a].append(b)
        else :
            conn[a] = [b]
        if b in conn :
            conn[b].append(a)
        else :
            conn[b] = [a]
            
    
    def dfs(breaknode: set):
        # startNode ==> just start from 1.
        visited = [False for i in range(n)]
        visited[0] = True
        stack = [1]
        
        # dfs
        while stack :
            curNode = stack.pop()
            # 안끊어진 노드, 방문안한 노드만 스택에 추가
            for nextNode in conn[curNode] :
                if not visited[nextNode-1] and breaknode != {curNode, nextNode} :
                    stack.append(nextNode)
                    visited[nextNode-1] = True
        return sum(visited)
    
    
    min = float('inf')
    
    for wire in wires :
        one = dfs(set(wire))
        dif = abs(n - 2*one)
        if min > dif :
            min = dif
    
    return min