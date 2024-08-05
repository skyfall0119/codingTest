
import re

def solution(user_id, banned_id):
    
    ## 불량 사용자 리스트 저장
    dup = set()
    
    ## 재귀함수
    # 제재 인덱스 별로.
    def check(banidx, user_list, out_list:set) :
        
        if banidx == len(banned_id) :
            dup.add(tuple(sorted(out_list)))
            return 1
        
        tmp = "^" + banned_id[banidx].replace("*", ".") + "$"

        # 남은 유저 리스트에서 아이디 검색.
        # 찾은 불량사용자 뺀 유저리스트, 불량사용자 더한 불량사용자 리스트, 다음 제재 인덱스.
        for uid in user_list :
            if re.findall(tmp, uid) : 
                check(banidx+1, user_list-{uid}, out_list | {uid})
        
    
    check(0, set(user_id), set())
    
    return len(dup)