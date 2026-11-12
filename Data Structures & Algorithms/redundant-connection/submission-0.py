class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = {}
        n = len(edges) 

        for node, adj in edges:
            if node in graph:
                graph[node].append(adj)
            
            else:
                graph[node] = [adj]
            
            if adj in graph:
                graph[adj].append(node)
            
            else:
                graph[adj] = [node]

        
        for i in range(len(edges) -1, -1, -1):
            node, adj = edges[i]
            graph[node].remove(adj)
            graph[adj].remove(node)

            print(edges[i])
            print(graph)

            print(self.dfs(graph, node, n))

            if self.dfs(graph, node, n):
                return edges[i]
            
            else:
                graph[node].append(adj)
                graph[adj].append(node)
    
    def dfs(self, graph: dict, node: int, n: int):
        print(node)

        visisted = set()
        stack = [node]

        while stack:
            node = stack.pop()
            
            if node in visisted:
                continue
            
            visisted.add(node)
            
            for adj in graph[node]:
                if adj not in visisted:
                    stack.append(adj)

        return len(visisted) == n



        