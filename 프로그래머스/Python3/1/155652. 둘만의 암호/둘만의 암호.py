def solution(s, skip, index):
    answer = []
    
    base = ord('a')
    top = ord('z')
    
    skip_set = set(skip)
    
    for c in s:
        cur = ord(c)
        cnt = 0
        
        while cnt < index:
            cur += 1
            if cur > top:
                cur = base
            
            if chr(cur) not in skip_set:
                cnt += 1
        
        answer.append(chr(cur))
    
    return ''.join(answer)