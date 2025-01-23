class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 1
        ptr1 = 0
        while ptr1 < len(nums) - 1:
            temp = 1
            ptr2 = ptr1 + 1
            while ptr2 < len(nums):
                if nums[ptr2] > nums[ptr1]:
                    temp += 1
                    ptr1 += 1
                    ptr2 += 1
                    if temp > l:
                        l = temp 
                else:
                    ptr1 = ptr2
                    ptr2 = ptr1 + 1
                    temp = 1
            ptr1 += 1
        return l