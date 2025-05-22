def split_uv(w):
    left, right = 0, 0
    for i, ch in enumerate(w):
        if ch == "(":
            left += 1
        else:
            right += 1
            
        if left == right:
            split_idx = min(i+1, len(w))
            return w[:split_idx], w[split_idx:]
    
    return w, ""

def correct_p(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  
            stack.pop() 

    return len(stack) == 0  
            


def solution(p):
    if p == "":
        return ""
    
    u,v = split_uv(p)
    
    if correct_p(u):
        return u + solution(v)

    else:
        tmp = "(" + solution(v) + ")"
        flip = u[1:-1].translate(str.maketrans("()" , ")("))
        return tmp + flip