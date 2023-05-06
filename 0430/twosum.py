num = [2, 7, 9, 11]
target = 9

# 2,7 / 2,9 / 2,11 
# 7,9 / 7,11
# 9,11

def twoSum(nums, target):
    for i in range(len(nums)-1): # O(N) 단계가 필요
        for j in range(i+1, len(nums)): # O(N) 단계가 필요
            if nums[i] + nums[j] == target:
                return [i, j]
# ->  O(n^2)

def twoSum(nums, target):
    for i, num in enumerate(nums): # O(N)
        res = target - num
        if res in num[i+1::]: # i+1번재 인덱스부터 끝까지 O(N)
            return [i, i+1+nums[i+1::].index(res)]
# ->  O(n^2)

# 2 [7, 9, 11]
# i => 0
# nums[i+1::].index(7) -> 0