def solution(clothes):
   
    dic = {}
    for _, category in clothes :
        if category in dic :
            dic[category] += 1
        else :
            dic[category] = 1
    

    answer = 1
    for cnt in dic.values() :
        answer *= (cnt+1)
    
    
    return answer-1

