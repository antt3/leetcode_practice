import heapq

def findKthLargest(self, nums: list[int], k: int) -> int:
    # Initial Solution
    # Time: O(n * log(k)) | Space: O(k)
    return heapq.nlargest(k, nums)[-1]