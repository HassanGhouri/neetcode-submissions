class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i: [] for i in range(numCourses)}

        for course, req in prerequisites:
            graph[course].append(req)

        
        visiting = set()
        visited = set()

        for course in range(numCourses):
            if course in visited:
                continue
                
            stack = [(course, False)]

            while stack:
                course, processed = stack.pop()

                if processed:
                    visiting.remove(course)
                    visited.add(course)
                    continue

                if course in visiting:
                    return False
                
                if course in visited:
                    continue

                visiting.add(course)
                stack.append((course, True))

                for req in graph[course]:
                    if req in visiting:
                        return False
                    
                    if req not in visited:
                        stack.append((req, False))

        return True
            

                

        