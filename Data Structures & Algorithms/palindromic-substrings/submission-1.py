class Solution:
    def countSubstrings(self, s: str) -> int:

        total_counts = 0


        # odd palidromes:
        for i in range(len(s)):
            left = i
            right = i
            count = 0

            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            
            total_counts += count

        # even palidromes:

        for i in range(len(s) - 1):
            left = i
            right = i + 1
            count = 0

            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            
            total_counts += count

        
        return total_counts






        