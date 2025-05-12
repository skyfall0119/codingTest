def solution(A,B):
    answer = 0
    
    A.sort(reverse=True)
    B.sort()
    
    while A:
        out = A.pop() * B.pop()
        answer += out

    return answer