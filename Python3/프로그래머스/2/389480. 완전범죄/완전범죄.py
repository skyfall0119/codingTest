def solution(info, n, m):
    answer = n
    
    visited = set()
    
    
    # dfs
    # iterate 값 => 물건 i, A흔적 a, B흔적 b 
    # initial
    stack = [(0, 0, 0)]
    
    while stack:
        i, a, b = stack.pop()
        
        # exit condition
        if (i, a, b) in visited: # 이미 본 세트
            continue
        visited.add((i,a,b))
        
        if a >= n or b >= m: # 잡힘
            continue
        
        if a >= answer: # 볼 필요 없음 ()
            continue
        
        if i == len(info): # 안잡히고 다 훔침. a 값 업데이트
            if a < answer:
                answer = a
            continue
            
        # push next step (A steal , B steal)
        stack.append((i+1, a+info[i][0], b))
        stack.append((i+1, a, b+info[i][1]))
    
    # 모든 시나리오에서 경찰에서 잡힘.
    if answer == n:
        return -1
    
    return answer