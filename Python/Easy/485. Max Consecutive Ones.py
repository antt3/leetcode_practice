class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # One Line Solution (Best Time I've Found)
        # return max((len(list(g)) for k, g in groupby(nums) if k == 1), default = 0)
        
        # Found Better Solution
        maxi = result = 0
        for num in nums:
            if num == 1:
                result += 1
                maxi = max(maxi, result)
            else:
                result = 0
        return maxi
        
        # Initial Solution
        # if len(nums) <= 2 or 0 not in nums:
        #     return sum(nums)
        # out = 0
        # l = 0
        # while l < len(nums) - 1:
        #     if nums[l] != 1:
        #         l += 1
        #         continue
        #     temp = 1
        #     r = l + 1
        #     while r < len(nums):
        #         if nums[r] != 1:
        #             l = r
        #             if out < temp:
        #                 out = temp
        #             break
        #         temp += 1
        #         r += 1
        #         if out < temp:
        #             out = temp
        #     l += 1
        # return out