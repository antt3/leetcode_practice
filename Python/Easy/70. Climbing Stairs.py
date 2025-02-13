class Solution:
    # Initial Solution
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)

    # Alternate Solution Using DFS
    # def climbStairs(self, n: int) -> int:

    #     def dfs(i):
    #         if i >= n:
    #             return i == n
    #         return dfs(i + 1) + dfs(i + 2)

    #     return dfs(0)
