class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ordering = {}
        count = 0

        for char in order:
            ordering[char] = count
            count += 1

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            match = True

            for j in range(len(word1)):
                if j < len(word2):
                    if ordering[word2[j]] != ordering[word1[j]]:
                        match = False

                        if ordering[word2[j]] < ordering[word1[j]]:
                            return False
                        
                        else:
                            break
            
            if match and len(word2) < len(word1):
                return False
        
        return True

