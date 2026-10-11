class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] will be the min total cost to get to that floor
        n = len(cost)
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1):
            if cost[i-1] + dp[i-1] < cost[i-2] + dp[i-2]:
                dp[i] = cost[i-1] + dp[i-1]
            
            else:
                dp[i] = cost[i-2] + dp[i-2]
    
        return dp[-1]
        