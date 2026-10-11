class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] is the number of what s can be decoded in upto that 
        # point

        n = len(s)
        dp = [0] * n

        if int(s[0]) != 0:
            dp[0] = 1

        for i in range(1, n):

            if int(s[i]) != 0:
                dp[i] += dp[i-1]
            
            if 10 <= int(s[i-1: i +1]) <= 26:
                dp[i] += dp[i-2] if i >= 2 else 1
        
        return dp[-1]