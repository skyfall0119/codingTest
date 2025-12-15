def solution(diffs, times, limit):
    answer = 1
    
    def solve_level(level) :
        total = 0
        for i, (d, t) in enumerate(zip(diffs, times)):
            if i == 0:
                prev = 0
            else :
                prev = times[i-1]

            # calc current puzzle
            if d > level :
                total += (prev+t) * (d-level) + t
            else :
                total += t



        # time limit
        if total > limit:
            return False
        return True

    
    ## binary search
    low, high = 1, max(diffs) # levels
    while low <= high :
        mid = (low + high) // 2
        
        if solve_level(mid) :
            
            answer = mid
            high = mid-1
        else :
            low = mid+1
        
    
    return answer