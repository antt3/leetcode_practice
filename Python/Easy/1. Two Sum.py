def twoSum(self, nums: list[int], target: int) -> list[int]:
    # Alternate Solution
    # Time: O(n) | Space: 0(n)
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

    # Initial Solution
    # Time: O(n) | Space: 0(n)
    # hm = {}
    # for i, v in enumerate(nums):
    #     for k in hm.keys():
    #         if (v + k) == target:
    #             return [hm[k], i]
    #     hm[v] = i