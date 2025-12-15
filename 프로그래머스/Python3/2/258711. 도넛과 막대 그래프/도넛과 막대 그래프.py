def solution(edges):
    
    root, donut, oneway, eight = 0,0,0,0


    # keys = 정점(간선있는). values = 간선
    dic = {}

    ## 모든 정점 딕셔너리로 
    # index 0. 나가는 간선. index 1 들어오는 간선.
    for start, dest in edges :

        if start not in dic :
            dic[start] = [1,0]
        else :
            dic[start][0]+=1

        if (dest not in dic):
            dic[dest] = [0,1]
        else :
            dic[dest][1]+=1.


        ## 들어오는 간선 없음. 생성정점
    for key in dic :
        if (dic[key][1] == 0 ) and (dic[key][0] >= 2):
            root = key
        # 나가는 간선 없음. 막대그래프    
        elif dic[key][0] == 0 :
            oneway+=1
        # 나가는거 2,  들어오는거 != 0 : 8자
        elif (dic[key][0] == 2 ) and (dic[key][1] != 0) :
            eight += 1

    ## 도넛 = 생성정점에서 나가는 간선 - 8자, 막대.
    donut = dic[root][0] - eight - oneway

    return root, donut, oneway, eight
