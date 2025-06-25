import heapq

def lastStoneWeight(self, stones: list[int]) -> int:
    # Initial Solution
    # Time: O(n * log(n)) | Space: O(n)
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        s1 = heapq.heappop(stones)
        s2 = heapq.heappop(stones)
        if s1 < s2:
            heapq.heappush(stones, s1 - s2)
    return -stones[0] if stones else 0