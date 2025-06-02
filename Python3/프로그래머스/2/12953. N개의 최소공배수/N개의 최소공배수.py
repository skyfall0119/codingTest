from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    answer = arr[0]
    for num in arr[1:] :
        answer = lcm(answer, num)
    
    
    return answer

