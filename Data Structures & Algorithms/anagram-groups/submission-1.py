class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for str1 in strs:
            key = tuple(sorted(str1))
            if key in seen:
                seen[key].append(str1)
            
            else:
                seen[key] = [str1]
        
        answer = []
        for key in seen.keys():
            answer.append(seen[key])
        
        return answer



        
        