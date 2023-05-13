# (예시)
# a = deque()
# for i  in range(5):
#     a.append(i)

# print(a)
# print(a.popleft())
# print(a)

from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

print(truck_weights)
truck_weights.reverse() # 문자열 뒤집기
print(truck_weights)

def solution(bridge_length, max_length, truck_weights) :
    time = 0
    total_weight = 0
    bridge = deque([0]*bridge_length)
    truck_weights.reverse() # 첫번째 대기 트럭이 맨 마지막 인덱스에 위치

    while truck_weights: # O(N)
        total_weights -= bridge.popleft() # O(1)

        if total_weights + truck_weights > total_weights :
            bridge.append(0); # O(1)
        else :
            truck = truck_weights.pop() # O(1)
            bridge.append(truck) # O(1)
            total_weights += truck
        
        time += 1

    return time + bridge_length