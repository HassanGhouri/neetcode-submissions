class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1
        
        for char in t:
            if char not in counts:
                return False
            counts[char] -= 1
            if counts[char] < 0:
                return False
        
        if sum(counts.values()) != 0:
            return False
        
        return True
        