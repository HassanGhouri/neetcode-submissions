# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []
            
        depths = {}
        queue = [(root, 0)]
        head = 0
        max_depth = 0
        ans = []

        while head < len(queue):
            node, depth = queue[head]
            head += 1

            if node == None:
                continue
            max_depth = max(depth, max_depth)
            
            if depth not in depths:
                depths[depth] = []
            
            depths[depth].append(node.val)

            if node.left:
                queue.append((node.left, depth +1))
            
            if node.right:
                queue.append((node.right, depth +1))
        
        for i in range(max_depth + 1):
            ans.append(depths[i])
        
        return ans
        



        