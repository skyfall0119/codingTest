from collections import defaultdict

def conv_to_min(t):
    h,m = t.split(":")
    return int(h) * 60 + int(m)
    

def solution(fees, records):
    answer = defaultdict(int)
    car_accum_time = defaultdict(list)
    
    # 입력값 파싱
    for record in records:
        time, car, inout = record.split(" ")
        car_accum_time[int(car)].append(conv_to_min(time))

    # 차량별
    for car, li_t in car_accum_time.items():
        # 마지막 출차시간 없을시 23:59 추가
        if len(li_t) % 2 != 0:
            li_t.append(conv_to_min("23:59"))
        # 누적시간 계산
        accum = 0
        for i in range(0, len(li_t), 2):
            accum += li_t[i+1] - li_t[i]
        
        # 요금 계산
        # 1. 기본시간보다 작으면 기본요금
        if accum <= fees[0]:
            answer[car] = fees[1]
        # 2. 
        else:
            # 기본시간/요금 계산
            accum -= fees[0]
            answer[car] += fees[1]
            # 단위시간/요금 계산
            q,r = divmod(accum, fees[2])
            if r > 0: 
                q+=1
            answer[car] += q * fees[3]
        
    # 차번호 정렬
    answer = [answer[key] for key in sorted(answer.keys())]        
    return answer