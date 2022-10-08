from typing import List
"""
Source: https://leetcode.com/problems/running-sum-of-1d-array/
Question:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums

CONSTRAINTS
    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums


"""
Verbal solution:
THe solution is simple, we just need to loop through the array and add the current value to the previous value and store it in the current index.
"""