from collections import deque

def solution(begin, target, words):
    answer = 0
    # no target
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, words, 0))
    # bfs
    while q:
        curword, wordlist, cnt = q.popleft()

        if curword == target:
            return cnt

        for word in wordlist:
            dif = 0
            for x,y in zip(curword,word):
                if x != y:
                    dif += 1
                if dif >= 2:
                    break
            if dif == 1:
                newlist = [i for i in wordlist if i != word]
                q.append((word, newlist, cnt+1))

    return answer