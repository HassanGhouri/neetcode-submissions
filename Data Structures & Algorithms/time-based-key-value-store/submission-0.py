class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp, value))
        
        else:
            self.dic[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if self.dic.get(key) == None:
            return ""

        left = 0
        right = len(self.dic[key]) - 1
        largest_smaller = float('-inf')
        largest_smaller_val = ""


        while left <= right:
            mid = (left + right) // 2

            if largest_smaller <= self.dic[key][mid][0] <= timestamp:
                largest_smaller = self.dic[key][mid][0]
                largest_smaller_val = self.dic[key][mid][1]
            
            if self.dic[key][left][0] <= timestamp <= self.dic[key][mid][0]:
                right = mid - 1
            
            else:
                left = mid + 1
        
        if largest_smaller == float('-inf'):
            return ""
        
        else:
            return largest_smaller_val




        
