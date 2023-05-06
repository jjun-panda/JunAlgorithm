bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

time = 0 # 시간
total_weight = 0 # 다리 위에 올라간 트럭 무게의 총합
bridge = [0]*bridge_length # 다리

# 모든 트럭이 통과할 때까지 반복
while len(truck_weights) > 0:
    # 다리에 올라간 트럭이 빠져나감
    tmp = bridge.pop(0) # 다리의 맨 앞에 있는 원소 제거
    # 총 무게에 다리를 빠져나간 트럭 무게 빼주기
    total_weight = total_weight - tmp
    # 트럭이 다리에 올라감
    if total_weight + truck_weights[0] > weight: # 다리에 올리지 못함
        bridge.append(0)
    else: # 다리에 올린다
        truck = truck_weights.pop(0)
        bridge.append(truck)
        total_weight += truck # 총 무게에 다리에 올라간 트럭 무게 더해주기
        
    # 시간 증가
    time += 1

time += bridge_length # 마지막 트럭이 지나갈 때까지 걸리는 시간
print(truck_weights)
print(bridge)
print(time)

def solution(bridge_length, weight, truck_weights):
    time = 0 # 시간
    total_weight = 0 # 다리 위에 올라간 트럭 무게의 총합
    bridge = [0]*bridge_length # 다리

    # 모든 트럭이 통과할 때까지 반복
    while len(truck_weights) > 0:
        # 다리에 올라간 트럭이 빠져나감
        tmp = bridge.pop(0) # 다리의 맨 앞에 있는 원소 제거
        # 총 무게에 다리를 빠져나간 트럭 무게 빼주기
        total_weight = total_weight - tmp
        # 트럭이 다리에 올라감
        if total_weight + truck_weights[0] > weight: # 다리에 올리지 못함
            bridge.append(0)
        else: # 다리에 올린다
            truck = truck_weights.pop(0)
            bridge.append(truck)
            total_weight += truck # 총 무게에 다리에 올라간 트럭 무게 더해주기
            
        # 시간 증가
        time += 1

    time += bridge_length # 마지막 트럭이 지나갈 때까지 걸리는 시간
    return time