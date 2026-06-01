class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited=[]
        for i in nums:
            if i not in visited:
                visited.append(i)
            else:
                return True
        return False 
