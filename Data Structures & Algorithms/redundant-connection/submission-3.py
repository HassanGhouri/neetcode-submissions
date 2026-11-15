class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        self.parent = [i for i in range(n+1)]

        for a, b in edges:
            root_a = self.find(a)
            root_b = self.find(b)

            if root_a == root_b:
                return [a, b]
            
            self.parent[root_b] = root_a


    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        
        return x

        




        


        