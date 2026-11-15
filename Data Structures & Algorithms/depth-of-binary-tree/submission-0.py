# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_depth = 1
        if not root:
            return 0
        
        else:
            return max(max_depth, self.dfs(root.left, 1), self.dfs(root.right, 1))


    def dfs(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth

        max_depth = depth + 1

        return max(max_depth, self.dfs(root.left, max_depth), self.dfs(root.right, max_depth))



        