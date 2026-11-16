class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp[i] is true if the first i characters of s can be constucted using words from 
        # word dict

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True


        for i in range(n+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        
        return dp[-1]
        