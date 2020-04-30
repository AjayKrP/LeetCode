#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        extra = {}
        for i in range(len(nums)): # O(n)
            tmp = target - nums[i] # 0(1)
            if (tmp in extra):
                return [extra[tmp], i]
            extra[nums[i]] = i

            
# worst case complexity
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         extra = {}
#         for i in range(len(nums)): # O(n)
#             for j in range(i + 1, len(nums)): #O(n)*O(n) = O(n^2)
#                 if (nums[j] == target - nums[i]):
#                     return [i, j]
