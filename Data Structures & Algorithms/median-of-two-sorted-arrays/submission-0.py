class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=sorted(nums1+nums2)
        n=len(num)//2
        if len(num)%2==0:
            ou=(float(num[n]+float(num[n-1])))/2
            return ou
        else:
            return num[n]