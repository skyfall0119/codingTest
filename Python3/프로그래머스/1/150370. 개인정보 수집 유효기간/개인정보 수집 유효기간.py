class Privacy():
    ## static terms
    terms = {}
    
    def __init__(self, date, term) :
        self.year, self.month, self.date = date.split(".")
        self.exp_date = date
        self.term = term
    
    @staticmethod
    def updateTerm(terms):
        for term in terms :
            a,b = term.split()
            Privacy.terms[a] = int(b)
    
    def isExpired(self, today):
        today_y, today_m, today_d = today.split(".")
        total_today = int(today_y)*12*28
        total_today += (int(today_m)) * 28 
        total_today += int(today_d)
        
        total_exp = int(self.year)*12*28
        total_exp += (int(self.month)+Privacy.terms[self.term]) * 28 
        total_exp += int(self.date)
        return total_exp <= total_today
        
        
    

def solution(today, terms, privacies):
    answer = []
    
    ## update terms dic
    Privacy.updateTerm(terms)
    
    for i, privac in enumerate(privacies) :
        date, term = privac.split()
        expired = Privacy(date, term).isExpired(today)
        if expired :
            answer.append(i+1)
    answer.sort()
    return answer
