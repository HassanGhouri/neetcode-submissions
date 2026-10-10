from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seen = {}

        for char in s:
            if char in seen:
                seen[char] += 1
            
            else:
                seen[char] = 1
        
        for char in t:
            if char in seen:
                seen[char] -= 1
            
            else:
                return False
        
        for key in seen.keys():
            if seen[key] != 0:
                return False
        
        return True
        
        

        