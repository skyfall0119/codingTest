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
        ## stack        
        calc_list = exp_list.copy()
        calc_list.reverse() # 앞에서부터 O(1) pop. 
        tmp_stack = []
        
        for opr in comb:
            while calc_list:
                item = calc_list.pop() 
                if item == opr:
                    res = handle_opr(tmp_stack.pop(), calc_list.pop(), item)
                    tmp_stack.append(res)
                else:
                    tmp_stack.append(item)
            calc_list = tmp_stack
            calc_list.reverse()
            tmp_stack = []
        
        answer = max(answer, abs(calc_list[0]))
    
    return answer