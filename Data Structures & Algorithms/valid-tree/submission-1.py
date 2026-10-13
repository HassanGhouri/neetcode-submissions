class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        visited = set()
        graph = {i: [] for i in range(n)}

        for node, adj in edges:
            graph[node].append(adj)
            graph[adj].append(node)

        stack = [(0, -1)]

        while stack:
            node, parent = stack.pop()

            if node in visited:
                continue
            
            visited.add(node)

            for adj in graph[node]:
                if adj != parent and adj not in visited:
                    stack.append((adj, node))
    
        return len(visited) == n

        

