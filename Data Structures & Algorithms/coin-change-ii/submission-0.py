class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[j][i] is the number of unique ways to make i up to the jth coin in coins

        n = len(coins)
        dp =[[0 for i in range(amount+1)] for i in range(n+1)]

        for j in range(n+1):
            dp[j][0] = 1

        for j in range(1, n+1):
            coin = coins[j-1]

            for i in range(1, amount + 1):
                dp[j][i] = dp[j-1][i]
                
                if i >= coin:
                    dp[j][i] += dp[j][i-coin]


        return dp[-1][-1]

