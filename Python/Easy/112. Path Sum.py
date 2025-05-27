def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    # Ideal Recursive Solution
    # Time: 0(n) | Space: 0(n)
    if not root:
        return False
        
    targetSum -= root.val
    return (self.hasPathSum(root.left, targetSum) or 
            self.hasPathSum(root.right, targetSum) or
            (not targetSum and not root.left and not root.right))

    # Initial Solution
    # Time: O(n) | Space: O(n)
    # if not root: return False
    # targetSum -= root.val
        
    # if self.hasPathSum(root.left, targetSum): return True
    # if self.hasPathSum(root.right, targetSum): return True
    # if not root.left and not root.right and targetSum == 0: return True

    # targetSum += root.val
    # return False