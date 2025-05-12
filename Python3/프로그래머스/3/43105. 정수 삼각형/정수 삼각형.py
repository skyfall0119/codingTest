def solution(triangle):
    
    level = 0
    
    while level < len(triangle)-1:
        for i in range(len(triangle[level])):
            if i == 0: # 첫번째
                triangle[level+1][i] += triangle[level][i]
            # 중간
            else: 
                triangle[level+1][i] += max(triangle[level][i-1], triangle[level][i])
            
            # 마지막
            if i == len(triangle[level])-1: 
                triangle[level+1][i+1] += triangle[level][i]
                
        level += 1
    
    return max(triangle[-1])