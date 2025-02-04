class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 0, 1
        for j in range(1, len(nums)):
            if nums[i] < nums[j]:
                nums[i + 1] = nums[j]
                i += 1
                k += 1
        return k