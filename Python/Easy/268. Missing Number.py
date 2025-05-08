def missingNumber(self, nums: list[int]) -> int:
    # Initial Solution
    nums_count = [0] * (len(nums) + 1)
    for num in nums:
        nums_count[num] = 1
        
    for i in range(len(nums_count)):
        if not nums_count[i]: return i