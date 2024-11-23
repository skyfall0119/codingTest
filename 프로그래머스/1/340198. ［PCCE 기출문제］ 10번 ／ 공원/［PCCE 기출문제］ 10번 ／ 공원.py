import numpy as np

def solution(mats, park):
    answer = -1
    ## 큰 돗자리부터.
    mats.sort(reverse=True)
    ## numpy
    park = np.array(park)
    
    for mat in mats :

        for i in range(0, park.shape[0]-mat+1):
            for j in range(0,park.shape[1]-mat+1) :
                # 돗자리 subarray
                sub_matrix = park[i:i+mat, j:j+mat]
                # 알파벳 있으면 패스.
                if np.any(np.char.isalpha(sub_matrix)):
                    continue  
                # 알파벳 없으면 리턴.
                else :
                    return mat
                    
    return answer

