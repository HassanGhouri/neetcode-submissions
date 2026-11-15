# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = self.dfs(root)
        ans2 = []
        
        for level in ans:
            ans2.append(level[-1])
        
        return ans2
    

    def dfs(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return []

        ans = [[root.val]]
        left_level = []
        right_level = []

        if root.left:
            left_level = self.dfs(root.left)
        
        if root.right:
            right_level = self.dfs(root.right)

        n = min(len(left_level), len(right_level))        
        for i in range(n):
            combined = left_level[i] + right_level[i]
            ans.append(combined)
        
        if len(left_level) > n:
            for i in range(n, len(left_level)):
                ans.append(left_level[i])
            
        else:
            for i in range(n, len(right_level)):
                ans.append(right_level[i])
        
        return ans



        