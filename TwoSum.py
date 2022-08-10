"""
Source: https://leetcode.com/problems/two-sum/
Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

CONSTRAINTS
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # print(nums[i], nums[j])
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


solution = Solution()
print(solution.twoSum([2, 5, 5, 11], 10))


"""
Verbal solution:
Was an Easy One. Realized one has to use each item to add other items in the list and not adding itself though.so i made use of two loop one to get current value for addition 
and another loop to go through the other element in the array to add current value and check if their sum gives our target.
Time Spent:3Min
Got excited and submitted.Failed realized i didnt handle some test cases of where the same integer existed in two places,came back and solved it in previous commits.
just putting this out for honesty. shameful though..
I Failed Thoth 🤕😭
"""
