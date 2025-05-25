import sys
sys.setrecursionlimit(10**6)

def find_y_max(nodeList):
    maxYind = 0
    for i in range(len(nodeList)) :
        if nodeList[i][1] > nodeList[maxYind][1] :
            maxYind = i
    return maxYind


def preorder(nodeList) :
    if len(nodeList) == 0 :
        return []

    maxYind = find_y_max(nodeList)
        
    left = preorder(nodeList[:maxYind])
    right = preorder(nodeList[maxYind+1:]) 
    
    ## 노드번호 반환
    ret = [nodeList[maxYind][2]]+left+right
    return ret

def postorder(nodeList) :
    if len(nodeList) == 0 :
        return []

    maxYind = maxYind = find_y_max(nodeList)
        
    left = postorder(nodeList[:maxYind])
    right = postorder(nodeList[maxYind+1:]) 
    
    ## 노드번호 반환
    ret = left+right+[nodeList[maxYind][2]]
    return ret


def solution(nodeinfo):
    
    ## x 로 정렬. 노드번호 추가.
    for i in range(len(nodeinfo)) :

        ## z = 노드번호
        nodeinfo[i].append(i+1)

        ## x좌표로 insertion sort
        for j in range(i,0,-1) :
            if nodeinfo[j-1][0] > nodeinfo[j][0] :
                nodeinfo[j-1], nodeinfo[j] = nodeinfo[j], nodeinfo[j-1] 
            else :
                break

    pre =  preorder(nodeinfo)
    post =  postorder(nodeinfo)
    
    return [pre, post]