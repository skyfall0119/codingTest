from collections import Counter
def solution(X, Y):
    answer = ''
    
    x_cnt = Counter(X)
    y_cnt = Counter(Y)
    
    intersected = set(x_cnt.keys()).intersection(set(y_cnt.keys()))
    
    if not intersected:
        return "-1"
    elif intersected == {"0"}:
        return "0"
    else:
        nums = sorted(intersected,reverse=True)
        for num in nums:
            answer += num * min(x_cnt[num],y_cnt[num])
        return answer
    