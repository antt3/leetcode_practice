def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Initial Solution
        # Time: 0(H) | Space: O(H)
        if not root or root.val == val: return root
        if root.val < val: return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)