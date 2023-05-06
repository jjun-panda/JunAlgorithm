nums = [2, 7, 9, 11]
target = 9

# def twoSum(nums, target):
#     for i in range(len(nums)-1): # O(N) 단계가 필요
#         for j in range(i+1, len(nums)): # O(N) 단계가 필요
#             if nums[i] + nums[j] == target:
#                 # return [i, j]
#                 print(nums[i],nums[j])

def twoSum(nums, target):
    dicts = {}
    # for i in range(len(nums)):  # O(N)
    #     dicts[nums[i]] = i
    # print(dicts)

    for i in range(len(nums)):  # O(N)
        res = target - nums[i]
        if res in dicts:    # O(1)
            return[i, dicts[res]]
            # print(i, dicts[res])
            
        dicts[nums[i]] = i
        # print(dicts)

# O(N + (N+1)) => O(2N) => O(N)
print(twoSum(nums, target))