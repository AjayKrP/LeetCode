class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        extra = {}
        for i in range(len(nums)): # O(n)
            tmp = target - nums[i] # 0(1)
            if (tmp in extra):
                return [extra[tmp], i]
            extra[nums[i]] = i
