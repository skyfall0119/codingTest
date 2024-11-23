import numpy as np

def solution(mats, park):
    answer = -1
    
    ## 큰 돗자리순
    mats.sort(reverse=True)
    ## numpy 변환
    park = np.array(park)
    
    for mat in mats :
        for i in range(0, park.shape[0]-mat+1):
            for j in range(0,park.shape[1]-mat+1) :
                # 돗자리 자리의 모든 인덱스가 -1 이면 리턴.
                if np.all(park[i:i+mat, j:j+mat] == "-1") :
                    return mat
                    
    return answer

