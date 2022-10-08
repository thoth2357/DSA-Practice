from typing import List

def pivotIndex(nums: List[int]) -> int:
    #final solution
    right_sum = sum(nums)
    left_sum = 0
    
    for i in range(len(nums)):
        right_sum -= nums[i] # as the index is moving towards the right, our right sum is decreasing
        if left_sum == right_sum: # if the left sum is equal to the right sum, we have found our pivot index
            return i 
        left_sum += nums[i] # as the index is moving towards the right, our left sum is increasing
    return -1

    #second solution..Time complexity low
    # t = [i for i in range(len(nums)) if sum(nums[:i]) == sum(nums[i+1:])]
    # if t:
    #     return t[0]
    # else:
    #     return -1
    
    #first solution...Time complexity low
    # for i in range(len(nums)):
    #     print(i)
    #     left_sum = sum(nums[:i])
    #     right_sum = sum(nums[i+1:])
    #     print(left_sum, right_sum)
    #     if left_sum == right_sum:
    #         return i

t = pivotIndex([1,7,3,6,5,6])
print(t)