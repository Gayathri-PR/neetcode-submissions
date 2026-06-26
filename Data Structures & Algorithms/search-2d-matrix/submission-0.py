class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1
        while l <= r:
            m = (l+r)//2
            row = m//cols
            col = m%cols
            v = matrix[row][col]
            if v == t:
                return True
            elif v < t:
                l = m+1
            else:
                r = m-1
        return False
        