class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] is the number of distict ways to reach that step

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2
        
        if n == 1:
            return dp[0]
        
        for i in range(2, n):
            dp[i] = dp[i-1]
            dp[i] += dp[i-2] 

        print(dp)

        return dp[n-1]


