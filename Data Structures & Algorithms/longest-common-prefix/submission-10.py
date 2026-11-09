class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        lcp = ""
        m = len(strs[0])
        st1 = strs[0]
        n = len(strs)

        for i in range(m):
            char = st1[i]

            for j in range(1, n):

                if len(strs[j]) - 1 < i:
                    return lcp
                
                if strs[j][i] != char:
                    return lcp

            lcp += char

        return lcp
        