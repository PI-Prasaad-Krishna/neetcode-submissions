class Solution:
    def findDuplicate(self, nums: nums[int]) -> int:
        seen=[False]*len(nums)
        for i in nums:
            if seen[i]:
                return i
            seen[i]=True