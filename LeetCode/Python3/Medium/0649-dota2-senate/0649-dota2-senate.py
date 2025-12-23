from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # initial count
        r = 0
        d = 0
        for i in senate:
            if i == "R":
                r+=1
            else:
                d+=1

        
        r_ban = 0
        d_ban = 0

        q = deque(list(senate))

        while True:
            item = q.popleft()

            #
            if item == 'R':
                if d == 0:
                    return "Radiant"

                if r_ban > 0: # banned
                    r_ban -= 1
                    r -= 1
                else: # ban next D
                    d_ban += 1
                    q.append(item)
            else: # 'D'
                if r == 0:
                    return "Dire"
                if d_ban > 0: # banned 
                    d_ban -= 1
                    d -= 1
                else: # ban next R
                    r_ban += 1
                    q.append(item)
            
                    

            

        

        