# n진수 제너레이터
def k_base_gen(n,k):
    res = ''
    while n > 0:
        n, r = divmod(n,k)
        if r != 0:
            res += str(r)
        elif res:
            yield int(res[::-1])
            res = ''
    
    if res:
        yield int(res[::-1])


#소수판별
def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    return sum(1 for num in k_base_gen(n,k) if is_prime(num))