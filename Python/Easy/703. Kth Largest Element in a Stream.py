import heapq

class KthLargest:
    # Initial Solution
    # Time: O(a * log(k)) | O(k)
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        # Improved Solution
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
        # Initial Solution
        # if not self.nums:
        #     self.nums.append(val)
        # if len(self.nums) == self.k:
        #     heapq.heappushpop(self.nums, val)
        # else:
        #     heapq.heappush(self.nums, val)
        # return self.nums[0]