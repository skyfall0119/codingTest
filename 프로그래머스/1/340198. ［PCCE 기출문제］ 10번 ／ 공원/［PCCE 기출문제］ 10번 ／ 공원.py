import numpy as np

def solution(mats, park):
    answer = -1
    
    mats.sort(reverse=True)
    park = np.array(park)
    print(park.shape)
    for mat in mats :

        for i in range(0, park.shape[0]-mat+1):
            for j in range(0,park.shape[1]-mat+1) :
                               
                sub_matrix = park[i:i+mat, j:j+mat]
                
                if np.any(np.char.isalpha(sub_matrix)):
                    continue  
                
                try:
                    sub_matrix_sum = sub_matrix.astype(float).sum()
                    return mat  
                except ValueError:
                    continue  
                    
    return answer

