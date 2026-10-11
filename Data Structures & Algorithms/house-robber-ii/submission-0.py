class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] will return the max amount of money you have have by the 
        # ith house
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])

        for i in range(2, n-1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        max_money = dp[n-2]

        dp = [0] * n
        dp[1] = nums[1]
        dp[2] = max(nums[2], dp[1])

        for i in range(3, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return max(max_money, dp[n-1])