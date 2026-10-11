class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        target = {}
        window = {}

        n = len(s2)
        window_len = len(s1)


        for char in s1:
            target[char] = target.get(char, 0) + 1
        
        left = 0

        for right in range(n):
            window[s2[right]] = window.get(s2[right], 0) + 1
        
            if (right - left + 1) > window_len:
                window[s2[left]] -= 1
            
                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1
            
            if window == target:
                return True
    
        return False
