class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        len_longest = 0

        left = 0
        right = 0
        seen = set()

        while right < len(s):
            if s[right] in seen:

                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1

                seen.remove(s[left])
                left += 1
                seen.add(s[right])
                right += 1
                len_longest = max(len_longest, right - left)
            
            else:
                seen.add(s[right])
                right += 1
                len_longest = max(len_longest, right - left)
        
        return len_longest
        