class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])


        dp = [[0 for i in range(n)] for i in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 1:
                    if i == 0 and j == 0:
                        continue


                    if i == 0:
                        dp[i][j] = dp[i][j-1]
                    
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    
                    else:
                        if obstacleGrid[i][j-1] != 1:
                            dp[i][j] += dp[i][j-1]
                        
                        if obstacleGrid[i-1][j] != 1:
                            dp[i][j] += dp[i-1][j]
        
        return dp[m-1][n-1]
        