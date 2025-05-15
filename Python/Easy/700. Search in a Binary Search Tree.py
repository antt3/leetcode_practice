def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    # Iterative Solution
    # Time: 0(log(n)) | Space: O(1)
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root
    
    # Initial Solution
    # Time: 0(log(n)) | Space: O(log(n))
    # if not root or root.val == val: return root
    # if root.val < val: return self.searchBST(root.right, val)
    # return self.searchBST(root.left, val)