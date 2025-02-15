from itertools import combinations
def solution(n, q, ans):
    answer = 0
    
    ## 1. 숫자 조합 생성 loop
    for num in combinations(range(1,n+1), 5):
        
        ## 2. 숫자 조합 일치 확인
        matching = True
        for question, res in zip(q, ans):
            if len(set(num) & set(question)) != res:
                matching = False
                break
    
        ## 3. 시스템 응답 일치시 answer += 1
        if matching:
            answer +=1
    
    
    return answer