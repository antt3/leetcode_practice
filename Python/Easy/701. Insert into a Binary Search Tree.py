def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    # Initial Solution
    # Time: 0(log(n)) | Space: O(log(n))
    if not root: return TreeNode(val)
    if root.val > val:
        root.left = self.insertIntoBST(root.left, val)
    else:
        root.right = self.insertIntoBST(root.right, val)
    return root