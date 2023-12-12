# -*- coding: utf-8 -*-
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        print(i)
        cnt = 0
        for j in range(1, i+1):
            print(j)
            if i % j == 0: # 나누어 떨어지는 수가 약수
                cnt += 1 # 약수의 개수를 증가 
        
        if cnt % 2 == 0: # 약수의 개수가 짝수이면 
            answer += i
        else:
            answer -= i

    return answer

left = 13
right = 17 
print(solution(left, right))
