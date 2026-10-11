from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_freq = Counter(t)
        window = {}

        have = 0
        need = len(t_freq)
        n = len(s)

        min_len = float('inf')
        left = 0
        result = (-1, -1)


        for right in range(n):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in t_freq and window[char] == t_freq[char]:
                have += 1

            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = (left, right)

                left_char = s[left]
                window[left_char] -= 1

                if left_char in t_freq and window[left_char] < t_freq[left_char]:
                    have -= 1
                
                left += 1

        l, r = result
        return s[l: r + 1] if min_len != float('inf') else ""


        









        