class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
    
        visisted = set()
        relations = {i: [] for i in range(n)}

        for node, adj in edges:
            relations[node].append(adj)
            relations[adj].append(node)

        stack = [(0, -1)]

        while stack:
            node, parent = stack.pop()
            
            if node in visisted:
                continue
            
            visisted.add(node)

            for adj in relations[node]:
                if adj != parent and adj not in visisted:
                    stack.append((adj, node))
    
        return len(visisted) == n

        