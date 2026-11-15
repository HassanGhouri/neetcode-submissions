class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)

        if m == 0:
            return False
        
        n = len(matrix[0])

        left = 0
        right = m-1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                left = mid
                right = mid
                break

            elif matrix[mid][n-1] < target:
                left = mid + 1
            
            elif matrix[mid][0] > target:
                right = mid - 1
        
        if left != right:
            return False
        
        row = left
        left = 0
        right = n-1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True

            if matrix[row][mid] < target:
                left = mid + 1
            
            if matrix[row][mid] > target:
                right = mid - 1
        
        return False

        