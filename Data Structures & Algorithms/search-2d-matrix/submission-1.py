class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        rows=len(matrix)
        cols=len(matrix[0])
        r=rows*cols-1
        while l<=r:
            m=(l+r)//2
            row_no=m//cols
            col_no=m%cols
            val=matrix[row_no][col_no]
            if target==val:
                return True
            if target>val:
                l=m+1
            if target<val:
                r=m-1
        return False
            


            

        
