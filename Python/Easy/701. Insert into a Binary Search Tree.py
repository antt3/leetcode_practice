def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    # My Iterative Solution
    # Time: O(log(n)) | Time: O(1)
    if not root: return TreeNode(val)
    temp = root
    while True:
        if temp.val < val:
            if not temp.right:
                temp.right = TreeNode(val)
                return root
            temp = temp.right
        else:
            if not temp.left:
                temp.left = TreeNode(val)
                return root
            temp = temp.left
    
    # Initial Solution
    # Time: 0(log(n)) | Space: O(log(n))
    # if not root: return TreeNode(val)
    # if root.val > val:
    #     root.left = self.insertIntoBST(root.left, val)
    # else:
    #     root.right = self.insertIntoBST(root.right, val)
    # return root