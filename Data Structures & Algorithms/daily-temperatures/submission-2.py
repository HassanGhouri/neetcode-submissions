class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        results = [0] * len(temperatures)

        for i in range(len(temperatures) -1, -1, -1):
            temp = temperatures[i]

            while stack and temp >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                results[i] = stack[-1] - i
            
            stack.append(i)
            
        
        return results
