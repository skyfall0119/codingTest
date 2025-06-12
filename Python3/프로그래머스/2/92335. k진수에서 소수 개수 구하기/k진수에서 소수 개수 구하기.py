from concurrent.futures import ProcessPoolExecutor, as_completed
def to_k_base(n,k):
    res = ""
    while n > 0:
        n, r = divmod(n,k)
        res += str(r)
    return res[::-1]



def is_prime(num):
    
    if num == 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True

def solution(n, k):
    
    converted = to_k_base(n,k)
    splited = [int(num) for num in converted.split("0") if num]
    
    with ProcessPoolExecutor(max_workers=10) as executor:
        results = executor.map(is_prime, splited)
    

    return sum(results)