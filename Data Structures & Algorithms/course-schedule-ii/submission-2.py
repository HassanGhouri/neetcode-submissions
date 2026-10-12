class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        ans = []
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
                    ans.append(course)
                    continue

                if course in visiting:
                    return []
                
                if course in visited:
                    continue
                
                visiting.add(course)
                stack.append((course, True))
                for req in graph[course]:
                    if req in visiting:
                        return []
                    
                    if req in visited:
                        continue
                    
                    stack.append((req, False))

            visiting = set()


        return ans if len(ans) == numCourses else []
                


            

        