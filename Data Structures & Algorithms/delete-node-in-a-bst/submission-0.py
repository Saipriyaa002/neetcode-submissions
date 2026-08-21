class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        # Search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Case 1: No left child
            if root.left is None:
                return root.right

            # Case 2: No right child
            if root.right is None:
                return root.left

            # Case 3: Two children
            # Find the smallest value in right subtree
            successor = root.right
            while successor.left:
                successor = successor.left

            # Replace current value
            root.val = successor.val

            # Delete the duplicate successor
            root.right = self.deleteNode(root.right, successor.val)

        return root