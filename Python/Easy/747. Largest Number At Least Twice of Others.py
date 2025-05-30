def dominantIndex(self, nums: List[int]) -> int:
    # Initial Solution
    # Time: O(n) | Space: O(1)
    res, big_i = 0, 0
    for cur_i in range(1, len(nums)):
        if nums[big_i] < nums[cur_i]:
            res = cur_i if (nums[big_i] * 2) <= nums[cur_i] else -1
            big_i = cur_i
        else:
            if (nums[cur_i] * 2) > nums[big_i]: res = -1
    return res