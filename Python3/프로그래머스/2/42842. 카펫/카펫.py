def solution(brown, yellow):
    answer = []
    w_h = int(brown / 2 -2 )
    
    if w_h == 2:
        return [3,3]
    
    for i in range(1, w_h-1):
        if yellow == i * (w_h-i):
            answer = [i+2, w_h-i+2]
            answer.sort(reverse=True)
            return answer
        
    
    
    return answer