class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[i] represents the number of ways to reach that coin


        if amount == 0:
            return 0

        if len(coins) == 0:
            return -1

        if min(coins) > amount:
            return -1
        
        dp = [0] * (amount + 1)

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount+1):
            for coin in coins:
                if coin <= amount:
                    if i > coin and dp[i-coin] != 0:
                        if dp[i] != 0:
                            dp[i] = min(dp[i-coin] + 1, dp[i])
                        else:
                            dp[i] = dp[i-coin] + 1
        
        print(dp)
        return dp[-1] if dp[-1] != 0 else -1
        