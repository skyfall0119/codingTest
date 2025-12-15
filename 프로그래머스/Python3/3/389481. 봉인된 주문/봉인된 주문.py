cycle = ord("z") - ord("a") + 1

# 문자열 -> 인덱스
def get_index(ban):
    ind = 0
    for ch in ban:
        ind = ind * cycle  + (ord(ch) - ord('a') + 1)
    
    return ind

# 인덱스 -> 문자열 
def get_str(ind):
    s = []
    while ind > 0:
        ind -= 1
        ind, remainer = divmod(ind, cycle)
        s.append(chr(ord('a') + remainer))
    
    return "".join(reversed(s))



def solution(n, bans):
    
    bans.sort(key= lambda x : (len(x), x))
    

    ## binary search from bans
    left, right = 0, len(bans)
    while left < right:
        mid = (left + right) // 2
        if get_index(bans[mid]) - mid > n:
            right = mid
        else:
            left = mid + 1
                
    return get_str(n + left)