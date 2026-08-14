"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        seen = {}

        return self.copy(node, seen)

    def copy(self, node, seen):
        n = Node(node.val)
        seen[n.val] = n

        for neighbor in node.neighbors:
            if neighbor.val not in seen.keys():
                temp = self.copy(neighbor, seen)
                n.neighbors.append(temp)
                # temp.neighbors.append(n)
            else:
                n.neighbors.append(seen[neighbor.val])
                
        return n