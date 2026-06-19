class Solution:
    def findDuplicate(self, nums: nums[int]) -> int:
        s={}
        for i in range(len(nums)):
            if nums[i] not in s:
                s[nums[i]]=1
            else:
                s[nums[i]]+=1
        for i in s:
            if s[i]>1:
                return i