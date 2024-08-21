import numpy as np
def solution(n, works) :
    max_val = max(works)
    arr = np.zeros((max_val, len(works)), dtype=int)
    for i, num in enumerate(works) :
        arr[:num, i] = 1

    
    ind = max_val-1

    for ind in range(max_val-1, -1, -1):
        # 제일 긴 시간?? 부터 체크
        
        indSum = arr[ind].sum()
        
        # 작업 시간 남음
        if indSum <= n :
            arr[ind].fill(0)
            n -= indSum
            
        # 작업시간 끝
        else :
            # 1 인 인덱스 찾기. n개만 사용
            indices = np.where(arr[ind] == 1)[0][:n]
            
            # 1 중에 남은 작업수만큼 0으로 변환
            for i in indices :
                arr[ind][i] = 0
            break

    ans = int(np.sum(np.square(np.sum(arr, axis=0))))
    return ans