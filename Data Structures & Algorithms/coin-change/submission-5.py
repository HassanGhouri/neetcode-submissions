class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] represents the few possible coins needed to get denom:

        if amount == 0:
            print("c")
            return 0

        if len(coins) == 0:
            print("b")
            return -1

        if amount < coins[0]:
            print("a")
            return -1
    
        dp = [float('inf')] * (amount + 1)

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        print(dp)
        for val in range(2, amount+1):
            for coin in coins:
                if val - coin >= 0:
                    dp[val] = min(dp[val], 1 + dp[val - coin])

        return dp[amount] if dp[amount] != float('inf') else -1


        