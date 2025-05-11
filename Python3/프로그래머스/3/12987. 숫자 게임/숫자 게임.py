from collections import deque
def solution(A, B):
    A.sort(), B.sort()
    aq = deque(A)
    bq = deque(B)


    cnt = 0
    while bq :

        if bq[0] > aq[0] :
            aq.popleft()
            bq.popleft()
            cnt+=1
        else : 
            bq.popleft()
            aq.pop()

    return cnt
