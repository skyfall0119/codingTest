from collections import defaultdict
import re
def solution(s):

    dic = defaultdict(int)
    nums = re.findall(r"\d+", s)
    
    for num in nums:
        dic[num] += 1
        
    answer = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    
    return [int(x[0]) for x in answer]