class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        right = 0
        longest_sub = 0
    
        while right < len(s):
            if s[right] not in freq:
                freq[s[right]] = 0
            
            freq[s[right]] += 1

            while (right - left + 1 - freq[max(freq,key=freq.get)]) > k:

                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                
                left += 1
            
            longest_sub = max(longest_sub, right - left + 1)
            right += 1
        
        return longest_sub

        