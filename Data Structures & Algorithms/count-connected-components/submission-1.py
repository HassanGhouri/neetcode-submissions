class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        self.parent = [i for i in range(n)]
        print(self.parent)
        count = n

        for a, b in edges:
            root_a = self.find(a)
            root_b = self.find(b)

            if root_a != root_b:
                self.parent[root_b] = root_a
                count -= 1

        #for i in range(len(self.parent)):
         #   self.parent[i] = self.find(self.parent[i])
        
        #ans = []

        #for i in self.parent:
         #   if i not in ans:
          #      ans.append(i)
        
        #return len(ans)
        return count


    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        
        return x
        