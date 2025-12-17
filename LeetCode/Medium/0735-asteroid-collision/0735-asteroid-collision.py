class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        temp = [] # going left asters.

        while asteroids:
            print(asteroids, ans, temp)
            one = asteroids.pop()
            if one > 0: # check temp for rightside
                if not temp: # farmost right. will never collide
                    ans.append(one)
                    continue

                while temp:
                    if abs(temp[-1]) > abs(one): # one lose
                        break
                    
                    elif abs(temp[-1]) < abs(one): # one win
                        temp.pop()
                        continue
                    # tie
                    temp.pop()
                    break
                else:
                    # one remains
                    ans.append(one)
            else: # goin left
                temp.append(one)
        
        temp.reverse()
        ans.reverse()
        temp.extend(ans)

        return temp
        

