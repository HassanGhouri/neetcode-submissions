class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] represents the few possible coins needed to get denom:
    
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for val in range(1, amount+1):
            for coin in coins:
                if val >= coin:
                    dp[val] = min(dp[val], 1 + dp[val - coin])

        return dp[amount] if dp[amount] != float('inf') else -1


        