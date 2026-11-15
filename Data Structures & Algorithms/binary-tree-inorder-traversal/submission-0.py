# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ans = []
        if root.left:
            ans += self.dfs(root.left)
        
        ans += [root.val]

        if root.right:
            ans += self.dfs(root.right)
        
        return ans


    def dfs(self, root: Optional[TreeNode]) -> List[int]:

            ans = []

            if root.left:
                ans += self.dfs(root.left)
            
            ans += [root.val]

            if root.right:
                ans += self.dfs(root.right)
            
            return ans

        