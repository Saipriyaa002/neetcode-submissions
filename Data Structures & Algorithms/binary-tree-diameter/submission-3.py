# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia=0
        def get_depth(node:Optional[TreeNode])->int:
            if not node:
                return 0
            ld=get_depth(node.left)
            rd=get_depth(node.right)
            self.max_dia=max(self.max_dia,ld+rd)
            return 1+max(ld,rd)
        get_depth(root)
        return self.max_dia


        '''self.dia=0
        def height(node):
            if not node:
                return 0
            l=height(node.left)
            r=height(node.right)
            self.dia=max(self.dia,l+r)
            return 1+max(l,r)
        height(root)
        return self.dia'''

        '''self.d=0
        def getDepth(node):
            if not node:
                return 0
            l=getDepth(node.left)
            r=getDepth(node.right)
            self.d=max(self.d,r+l)
            return 1+max(l,r)
        getDepth(root)
        return self.d'''
                
