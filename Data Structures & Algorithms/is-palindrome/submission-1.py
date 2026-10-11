class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s1 = s.lower()

        while left < right:
            if not s1[left].isalnum():
                left += 1
                continue
            
            if not s1[right].isalnum():
                right -= 1
                continue

            if s1[left] != s1[right]:
                print(left, right, s1[left], s1[right])
                return False
            
            left += 1
            right -= 1
        
        return True
        