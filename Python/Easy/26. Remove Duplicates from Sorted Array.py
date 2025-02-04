class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Alternate Solution
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
        
        # Refactored Solution
        # i = 1
        # for j in range(1, len(nums)):
        #     if nums[i - 1] < nums[j]:
        #         nums[i] = nums[j]
        #         i += 1
        # return i
        
        # Initial Solution
        # i, k = 0, 1
        # for j in range(1, len(nums)):
        #     if nums[i] < nums[j]:
        #         nums[i + 1] = nums[j]
        #         i += 1
        #         k += 1
        # return k