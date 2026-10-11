class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        perm = tuple(sorted(s1))
        window_len = len(perm)
        n = len(s2)

        left = 0

        for right in range(window_len - 1, n):
            if tuple(sorted(s2[left: right + 1])) == perm:
                return True
            
            else:
                left += 1
        
        return False

        