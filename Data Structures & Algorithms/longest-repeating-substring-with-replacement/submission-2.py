class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = {}
        n = len(s)
        longest = 0
        left = 0

        for right in range(n):
            counts[s[right]] = counts.get(s[right], 0) + 1

            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            
            longest = max(right - left + 1, longest)
        
        return longest







        