def solution(expressions):
    answer = []
    
    ## 진수 찾기 계산
    def calc(a,b,op,base) :
        if op =="+" :
            return int(a, base) + int(b, base)
        elif op == "-" :
            return int(a, base) - int(b, base)

    ## n진수로 변환
    def convBase(num, base) :
        if num == 0 :
            return 0
        res = ""
        while num > 0 :
            num, mod = divmod(num, base)
            res = str(mod)+res
        return res
            
    xList = []
    bases = {i for i in range(2,10)}
    for exp in expressions :
        a, op, b, _, out = exp.split()
        maxChar = "0"
        for char in a+b :
            maxChar = char if char > maxChar else maxChar
        
        bases -= {i for i in range(2, int(maxChar)+1)}
        # bases -= initialOut
        
        # ## X 문제일때 문제리스트에 추가
        if out == "X" : 
            xList.append(exp)

        ## 답이 있는문제. 진수 찾기
        else :
            minus = set()
            for base in bases :
                try :
                    expCalc = calc(a,b,op,base)
                    if expCalc != int(out, base) :
                        minus.add(base)
                except ValueError :
                    minus.add(base)
            bases -= minus
    
    
    ## X 문제리스트 풀기
    
    # 진수확정
    if len(bases) == 1 : 
        base = bases.pop()
        for exp in xList :
            a, op, b, _, out = exp.split()
            res = convBase(calc(a,b,op, base), base)
            answer.append(f"{a} {op} {b} = {res}")
        
        
    ## 몇진수인지 확정안남. 싹 계산
    else:
        for exp in xList :
            a, op, b, _, out = exp.split()
            baselist = list(bases)
            

            ans = set()
            while baselist :
                base = baselist.pop()
                ans.add(convBase(calc(a,b,op, base), base))

            if len(ans) == 1 :
                answer.append(f"{a} {op} {b} = {ans.pop()}")
            else :
                answer.append(f"{a} {op} {b} = ?")

    return answer