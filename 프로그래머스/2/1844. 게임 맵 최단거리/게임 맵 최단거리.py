from collections import deque

def solution(maps):
    answer = len(maps) * len(maps[0]) +1
    
    q = deque([(0,0,0)]) # 초기 위치 x,y + 거리
    dxdy = [(1,0), (-1,0), (0,1), (0,-1)]
    
    maps[0][0] = 0
    
    
    #bfs
    while q :
        x,y,d= q.popleft()
        
        # 목표위치 도달
        if x == len(maps[0])-1 and y == len(maps)-1 :
            return d+1
        
        for dx, dy in dxdy :
            x2, y2 = x+dx, y+dy
            if 0<= x2 < len(maps[0]) and 0<= y2 < len(maps) and maps[y2][x2] == 1:
                
                maps[y2][x2] = 0 # 방문
                
                q.append((x2, y2, d+1)) 


    return -1