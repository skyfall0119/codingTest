

def solution(players, m, k):
    answer = 0

    def remove_expired_servers(servers, cur):
        ## option1: pop
#         while servers and servers[0] + k <= cur:
#             servers.pop(0)
#         return servers
    
        ## option2: 슬라이싱
        i = 0
        while i < len(servers) and servers[i] + k <= cur:
            i += 1
        return servers[i:]
    
        
        
    servers = []
        
    for cur_time, num_player in enumerate(players):
        # update server
        servers = remove_expired_servers(servers, cur_time)
        
        # check for server increase. and increase if need
        max_num = m * (len(servers)+1)-1 # 현재 수용가능한 게임 이용자 수
        
        # 수용가능 인원 초과시
        if num_player > max_num:
            # 증설 필요 수
            needed = (num_player - max_num + m-1) // m
            answer += needed
            for _ in range(needed):
                servers.append(cur_time)
        

    return answer