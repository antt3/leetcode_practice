class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) <= 2 or 0 not in nums:
            return sum(nums)
        out = 0
        l = 0
        while l < len(nums) - 1:
            if nums[l] != 1:
                l += 1
                continue
            temp = 1
            r = l + 1
            while r < len(nums):
                if nums[r] != 1:
                    l = r
                    if out < temp:
                        out = temp
                    break
                temp += 1
                r += 1
                if out < temp:
                    out = temp
            l += 1
        return out