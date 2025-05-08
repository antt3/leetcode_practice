def sortColors(self, nums: list[int]) -> None:
        # Initial Solution
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]
        for i in range(len(nums)):
            colors[nums[i]] = colors[nums[i]] + 1

        i = 0
        for j in range(3):
            for k in range(colors[j]):
                nums[i] = j
                i += 1