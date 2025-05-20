def conv_n_base(num, base):
    res = ''
    if num == 0:
        return '0'
    while num > 0:
        num, mod = divmod(num, base)
        
        if mod >= 10:
            mod = chr(ord('A') + (mod - 10))
            
        res += str(mod)
    return res[::-1]
        
    

def solution(n, t, m, p):
    answer = ''
    num = 0
    turn = 1
    while True:
        converted = conv_n_base(num, n)
        
        for ch in converted:
            if p == turn:
                answer += ch
                if len(answer) == t:
                    return answer
            turn = (turn % m) +1
        
            
        num += 1
        

    return answer