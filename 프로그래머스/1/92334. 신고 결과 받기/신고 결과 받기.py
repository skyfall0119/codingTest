from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    usrs = defaultdict(dict)
    #### usr dict init
    for uid in id_list :
        usrs[uid]['reported_by'] = set()
        usrs[uid]['result'] = 0
    
    #### uar report update
    for r in report :
        usr, reported_usr = r.split(" ")
        usrs[reported_usr]['reported_by'].add(usr)

    #### check ban status        
    for usr, info in usrs.items():
        if len(info['reported_by']) >= k :
            for u in info['reported_by'] :
                usrs[u]['result'] += 1
    #### answer
    for usr, info in usrs.items():
        answer.append(info['result'])
    return answer