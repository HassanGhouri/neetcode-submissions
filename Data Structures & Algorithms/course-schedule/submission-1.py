class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)
        
        visiting = set()
        visited = set()

        for course in range(numCourses):
            if course in visited:
                continue
        
            stack = [(course, False)]

            while stack:
                node, processed = stack.pop()

                if processed:
                    visiting.remove(node)
                    visited.add(node)
                    continue
                

                if node in visiting:
                    return False
                
                if node in visited:
                    continue
                
                visiting.add(node)
                stack.append((node, True))

                for pre in graph[node]:
                    if pre in visiting:
                        return False

                    if pre not in visited:
                        stack.append((pre, False))


        return True                

        
        