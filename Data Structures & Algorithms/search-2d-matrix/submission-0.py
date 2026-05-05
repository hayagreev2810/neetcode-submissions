class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        total_el=rows*cols
        l=0
        r=total_el-1
        while l<=r:
            m=l+(r-l)//2
            row_no=m//cols
            col_no=m%cols
            if target==matrix[row_no][col_no]:
                return True
            elif target>matrix[row_no][col_no]:
                l=m+1
            else:
                r=m-1
        return False
      


        