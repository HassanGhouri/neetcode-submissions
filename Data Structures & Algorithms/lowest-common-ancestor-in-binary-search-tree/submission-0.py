# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        graph = {}
        stack = [(root, -1)]

        while stack:
            node, parent = stack.pop()
            graph[node] = parent

            if node.left:
                stack.append((node.left, node))
            
            if node.right:
                stack.append((node.right, node))
        
        q_chain = []
        q_parent = q

        while q_parent != -1:
            q_chain.append(q_parent)
            q_parent = graph[q_parent]

        p_chain = set()
        p_parent = p

        while p_parent != -1:
            p_chain.add(p_parent)
            p_parent = graph[p_parent]

        for i in q_chain:
            if i in p_chain:
                return i
        



            

