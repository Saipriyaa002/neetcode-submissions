# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,m):
            c=0
            if node is None:
                return 0
            if (node.val>=m):
                c=1
                m=node.val
            c+=dfs(node.left,m)
            c+=dfs(node.right,m)
            return c
        return dfs(root,root.val)