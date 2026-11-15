# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diam = 0
        self.dfs(root, 0)
        
        return self.max_diam

    def dfs(self, root: Optional[TreeNode], depth: int) -> int:

        if root == None:
            return depth
        
        depth += 1
        left_depth = 0
        right_depth = 0

        left_depth = self.dfs(root.left, depth)
        right_depth = self.dfs(root.right, depth)
        
        root_diam = left_depth - depth + right_depth - depth

        self.max_diam = max(root_diam, self.max_diam)

        return max(left_depth, right_depth)



