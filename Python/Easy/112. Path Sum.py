def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    # Initial Solution
    # Time: O(n) | Space: O(n)
    if not root: return False
    targetSum -= root.val
        
    if self.hasPathSum(root.left, targetSum): return True
    if self.hasPathSum(root.right, targetSum): return True
    if not root.left and not root.right and targetSum == 0: return True

    targetSum += root.val
    return False