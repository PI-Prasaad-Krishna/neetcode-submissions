class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        left=0
        lseen={}
        for right, c in enumerate(s):
            if c in lseen and lseen[c]>=left:
                left=lseen[c]+1
            max_length=max(max_length,right-left+1)
            lseen[c]=right
        return max_length