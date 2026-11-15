# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []

        graph = {}
        queue = [(root, 0)]
        max_depth = 0
        head = 0
        ans = []

        while len(queue) > head:
            node, depth = queue[head]
            head += 1

            if node is None:
                continue
            
            if depth not in graph:
                graph[depth] = []
            
            graph[depth].append(node.val)

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
            max_depth = max(max_depth, depth)
        
        for i in range(max_depth + 1):
            ans.append(graph[i][-1])
        
        return ans

        