def twoSum(self, nums: list[int], target: int) -> list[int]:
    # Initial Solution
    # Time: O(n) | Space: 0(n)
    hm = {}
    for i, v in enumerate(nums):
        for k in hm.keys():
            if (v + k) == target:
                return [hm[k], i]
        hm[v] = i