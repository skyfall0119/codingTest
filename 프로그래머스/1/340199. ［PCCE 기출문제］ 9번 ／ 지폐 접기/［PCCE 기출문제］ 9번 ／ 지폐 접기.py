def solution(wallet, bill):
    answer = 0
    
    def check_fit(w, b):
        return max(w) >= max(b) and min(w) >= min(b)
    
    while not check_fit(wallet,bill):
        bill = [int(max(bill)/2), min(bill)]
        answer+=1
        
    return answer