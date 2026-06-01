class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        low=0
        high=row*col-1
        while high>=low:
            mid=(low+high)//2
            r=mid//col
            c=mid%col
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                low=mid+1
            else:
                high=mid-1
        return False
        
