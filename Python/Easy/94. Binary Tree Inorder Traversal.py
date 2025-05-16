def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # Inital Solution
        # Time: O(n) | Space: O(n)
        if not root: return []
        l = self.inorderTraversal(root.left)
        l += [root.val]
        l += (self.inorderTraversal(root.right))
        return l