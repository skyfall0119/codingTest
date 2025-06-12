def to_k_base(n,k):
    res = ""
    while n > 0:
        n, r = divmod(n,k)
        res += str(r)
    return res[::-1]

def is_divisible(i, num):
    return num % i == 0

def is_prime(num):
    
    if num == 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        
    return True

def solution(n, k):
    answer = 0
    converted = to_k_base(n,k)
    
    for num in converted.split("0"):
        if not num:
            continue
        if is_prime(int(num)):
            answer += 1
    
    return answer