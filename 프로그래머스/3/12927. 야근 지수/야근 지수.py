import numpy as np
def solution(n, works) :

    works.sort(reverse=True)
    arr = np.array(works)
    total = arr.sum()-n

    if total <= 0 :
        return 0
    else :
        lastInd = len(arr)-1
        while True :

            if arr[lastInd] == 0 :
                lastInd -= 1

            else :
                if total > lastInd+1 :
                    
                    arr[:lastInd+1] -=1
                    total -= lastInd+1
                else :
                    arr[:total] -= 1
                    break
                    
    return int(np.sum( np.square(np.array(works) - arr)))