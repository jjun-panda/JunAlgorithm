from collections import deque

priorities = [2,1,3,2]
location = 2

def solution(priorities, location):
    priorities_deque = deque(priorities)
    process = [0]*len(priorities)
    process[location] = 1 # 몇번째로 실행되는지 알고자하는 프로세스의 위치를 1로 설정
    process_deque = deque(process)

    cnt = 0
    while priorities_deque : #O(N)
        p = priorities_deque.popleft() # 대기 1번 프로세스의 우선순위
        t = process_deque.popleft() # 대기 1번 프로세스
        if priorities_deque and max(list(priorities_deque)) > p : # 맨 마지막 순서가 됨
            priorities_deque.append(p)
            process_deque.append(t)
        else : # 본인이 마지막 순서이거나 우선순위가 제일 높은 경우
            cnt += 1
            if t == 1: #실행시킨 프로세스가 1이라면,
                break
    
    return cnt