from collections import defaultdict

class Robot() :
    
    ## class variable
    point_dic = None
    
    def __init__ (self, routes):
        self.routes = routes
        self.routes.reverse()
        self.start = self.__class__.point_dic[self.routes.pop()]
        self.dest = self.__class__.point_dic[self.routes.pop()]
        self.cur = self.start.copy()
        self.arrived = False

        
    def move(self) :
        ## move row first

        if self.cur[0] != self.dest[0] :
            self.cur[0] = self.cur[0]+1 if self.cur[0] < self.dest[0] else self.cur[0]-1
        ## move col
        elif self.cur[1] != self.dest[1] :
            self.cur[1] = self.cur[1]+1 if self.cur[1] < self.dest[1] else self.cur[1]-1

        # if dest arrived
        if self.cur[0] == self.dest[0]  and self.cur[1] == self.dest[1] :
            if self.routes : # if next dest exist, update
                self.dest = self.__class__.point_dic[self.routes.pop()]
            else : # if final dest
                self.arrived = True
    

def checkCollision(robots : list) :
    curLoc = defaultdict(int)
    for robot in robots :
        x,y = robot.cur
        curLoc[(x,y)] += 1
    cnt = 0
    for i in curLoc.values() :
        if i > 1 :
            cnt += 1
    return cnt
        
    
def solution(points, routes):
    answer = 0
    
    # save points in dic.
    point_dic = defaultdict()
    for i, loc in enumerate(points) :
        point_dic[i+1] = loc
        
    # to Robot class static variable
    Robot.point_dic = point_dic
    # init robot
    robots = [Robot(route) for route in routes]
    
    
    while robots :
        ## check collision
        answer += checkCollision(robots)
        
        ## remove arrived robot
        robots = [robot for robot in robots if not robot.arrived]
        
        # move robots
        for robot in robots :
            robot.move()

    
    return answer