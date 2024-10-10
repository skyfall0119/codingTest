from collections import deque
import numpy as np

def solution(maze):
    

    ## move function
    def canMove(red, blue):
        rmoves, bmoves, rbmoves = [], [], []
        rx, ry = red[0]  # red current pos
        bx, by = blue[0]  # blue current pos
        r_arrived = red[0] == dic['re']
        b_arrived = blue[0] == dic['be']

        ## check each direction
        for dx, dy in dxdy:
            # red moves
            nrx, nry = rx + dx, ry + dy
            if 0 <= nrx < len(red[1]) and 0 <= nry < len(red[1][0]): # boundary check
                if red[1][nrx][nry] != 1:  # not visited, 
                    if not r_arrived:  # not arrived
                        rmoves.append((nrx, nry))

            # blue moves
            nbx, nby = bx + dx, by + dy
            if 0 <= nbx < len(blue[1]) and 0 <= nby < len(blue[1][0]): # boundary check
                if blue[1][nbx][nby] != 1:  # not visited
                    if not b_arrived:  # not arrived
                        bmoves.append((nbx, nby))

        
        ## combine red blue moves
        # red + blue move
        if not r_arrived and not b_arrived :
            for rdx, rdy in rmoves:
                for bdx, bdy in bmoves:
                    if (rdx, rdy) == (bx, by) and (bdx,bdy) == (rx,ry) : ## if crossing. pass
                        continue
                    elif (rdx, rdy) != (bdx, bdy):  # No overlapping
                        rbmoves.append((rdx, rdy, bdx, bdy))

        # red move only
        elif not r_arrived and b_arrived:
            for rdx, rdy in rmoves:
                if (rdx, rdy) != dic['be']: ## can't pass blue wagon
                    rbmoves.append((rdx, rdy, bx,by))
                
        # blue move only
        elif not b_arrived and r_arrived :
            for bdx, bdy in bmoves :
                if (bdx, bdy) != dic['re']:## can't pass red wagon
                    rbmoves.append((rx,ry, bdx, bdy))
                
        return rbmoves


    ## init variables
    q = deque()
    dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = np.zeros((len(maze), len(maze[0])), dtype=int)
    dic = {}
    
    # maze
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                dic['rs'] = (i, j)  # Red start
            elif maze[i][j] == 2:
                dic['bs'] = (i, j)  # Blue start
            elif maze[i][j] == 3:
                dic['re'] = (i, j)  # Red end
            elif maze[i][j] == 4:
                dic['be'] = (i, j)  # Blue end
            elif maze[i][j] == 5:
                visited[i, j] = 1  # walls (=visited)

    # init red, blue
    red = [dic['rs'], visited.copy()]
    blue = [dic['bs'], visited.copy()]

    # mark start pos as visited
    red[1][red[0][0], red[0][1]] = 1
    blue[1][blue[0][0], blue[0][1]] = 1

    # q init for start.
    q.append((red, blue, 0))


    ## bfs
    while q:
        red, blue, cnt = q.popleft()
                
        # Check red blue arrive
        if red[0] == dic['re'] and blue[0] == dic['be']:
            return cnt

        # get possible moves
        moves = canMove(red, blue)

        # Process moves
        cnt += 1
        for rx, ry, bx, by in moves:
            new_red = [(rx, ry),red[1].copy()]
            new_blue = [(bx, by), blue[1].copy()]
            new_red[1][rx, ry] = 1
            new_blue[1][bx, by] = 1
            q.append((new_red, new_blue, cnt))

    return 0  # can't reach final destination with all moves