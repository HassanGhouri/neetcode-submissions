class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
        out = []
        visiting = set()
        visisted = set()

        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for course in range(numCourses):
            stack = [(course, False)]

            while stack:
                course, status = stack.pop()

                if status:
                    visiting.remove(course)
                    visisted.add(course)
                    out.append(course)
                    continue

                if course in visiting:
                    return []

                if course in visisted:
                    continue
                
                visiting.add(course)
                stack.append([course, True])

                for req in graph[course]:
                    if req in visiting:
                        return []
                        
                    if req not in visisted:
                        stack.append((req, False))

            visiting = set()
            
        return out if len(out) == numCourses else []
                




