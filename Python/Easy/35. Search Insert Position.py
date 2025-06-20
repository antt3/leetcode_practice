def searchInsert(self, nums: list[int], target: int) -> int:
    # Initial Solution
    # Time: O(log(n)) | Space: O(1)
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + ((r - l) // 2)
        if nums[m] == target: return m
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return l