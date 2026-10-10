class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        longest = 0
        curr = 0

        left = 0
        right = 0

        while right != len(s):

            if s[right] in seen:
                longest = max(curr, longest)
                while s[left] != s[right]:
                    seen.remove(s[left])
                    curr -= 1
                    left += 1
                
                seen.remove(s[left])
                left += 1
                curr -= 1

                
            else:
                seen.add(s[right])
                right += 1
                curr += 1
        
        return max(longest, curr)
            