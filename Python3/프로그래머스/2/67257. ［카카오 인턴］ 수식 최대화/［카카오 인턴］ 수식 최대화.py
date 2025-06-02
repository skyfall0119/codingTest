from itertools import permutations

def handle_opr(a,b,opr):
    if opr == "*":
        return a*b
    elif opr == "-":
        return a-b
    elif opr == "+":
        return a+b

def solution(expression):
    answer = 0
    exp_list = []
    
    # convert expression to list 
    tmp = ""
    for ch in expression:
        if ch not in "*-+":
            tmp += ch
        else:
            exp_list.append(int(tmp))
            exp_list.append(ch)
            tmp = ""
            
    # last number
    exp_list.append(int(tmp))

    
    ## calculate result from each combo
    for comb in permutations(["*", "+", "-"]):
        calc_list = exp_list.copy()
        for opr in comb:
            while True:
                try:
                    ind = calc_list.index(opr)
                    res = handle_opr(calc_list[ind-1], calc_list[ind+1], opr)
                    calc_list[ind-1] = res
                    calc_list.pop(ind)
                    calc_list.pop(ind)
                except: # no operator anymore
                    break
                    
        answer = max(answer, abs(calc_list[0]))
    
    return answer