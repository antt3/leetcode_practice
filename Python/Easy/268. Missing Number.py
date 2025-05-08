def missingNumber(self, nums: list[int]) -> int:
    # My Refactored Solution
    # Time: O(n) Space: O(1)
    t_num = (len(nums) * (len(nums) + 1)) / 2
    nums_sum = 0
    for num in nums:
        nums_sum += num
    return int(t_num - nums_sum)
    
    # Initial Solution
    # Time: O(n) Space: O(n)
    # nums_count = [0] * (len(nums) + 1)
    # for num in nums:
    #     nums_count[num] = 1
        
    # for i in range(len(nums_count)):
    #     if not nums_count[i]: return i