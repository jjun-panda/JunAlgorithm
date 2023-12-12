numbers = [1,2,3,4,6,7,8,0]

def solution(numbers):
    answer = 0
    for num in range(1, 10): # O(N)
        if num not in numbers: #O(N)
            answer += num 

    return answer


def solution2(numbers):
    comp = set([0,1,2,3,4,5,6,7,8,9])
    nums = set(numbers)
    cands = comp - nums
    answer = 0
    for c in cands:
        answer += c

    return answer

solution2(numbers)

def solution3(numbers):
    return 45 - sum(numbers) # sum -> O(N)

