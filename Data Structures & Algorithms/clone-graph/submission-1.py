"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        queue = []
        cloned = {}

        if node == None:
            return None

        new_top = Node(node.val)
        cloned[new_top.val] = new_top

        queue.append((new_top, node))

        while queue:
            new, node = queue.pop(0)

            for neighbor in node.neighbors:
                
                if neighbor.val not in cloned:
                    new_neighbor = Node(neighbor.val)
                    cloned[neighbor.val] = new_neighbor
                    queue.append((new_neighbor, neighbor))

                new.neighbors.append(cloned[neighbor.val])
        
        return new_top

        