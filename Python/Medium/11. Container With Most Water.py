def maxArea(self, height: list[int]) -> int:
    # Initial Solution
    # Time: O(n) | Space: O(1)
    res, l, r = 0, 0, len(height) - 1
    while l < r:
        tmp = min(height[l], height[r]) * (r - l)
        if res < tmp:
            res = tmp
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return res