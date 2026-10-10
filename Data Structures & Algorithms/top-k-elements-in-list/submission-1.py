class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            
            else:
                counts[num] = 1
        
        res = []
        for key, value in counts.items():
            res.append((key, value))
        
        res.sort(reverse=True, key=lambda word: word[1])

        answer = []

        for i in range(k):
            answer.append(res[i][0])

        return answer
        
