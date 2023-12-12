def solution(nums):
    #정렬 
    sorted_nums = sorted(nums)
    
    print(sorted_nums)

    # 원소: 인덱스 
    dicts = {}
    for i, n in enumerate(sorted_nums): #O(N)
        if n not in dicts: # O(1)
            dicts[n] = i
    print(dicts)

    answer = []
    for n in nums: #O(N)
        answer.append(dicts[n])

    return [dicts[n] for n in nums] # list comprehension: [(변수를 활용한 값) for (사용할 변수 이름) in (순회할 값)]

nums = [8,1,2,2,3]
print(solution(nums))

def solution2(nums):
    answer = []
    for n in nums:
        count = 0 
        for i in range(len(nums)):
            if n > nums[i]:
                count += 1
        
        answer.append(count)
    
    return answer


