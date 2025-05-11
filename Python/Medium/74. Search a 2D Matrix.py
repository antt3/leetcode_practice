def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    # Initial Solution
    # Time: O(log(m * n)) Space: O(1)
    for n in matrix:
        l , r = 0, len(n) - 1
        if n[r] < target:
            continue
        while l <= r:
            m = l + ((r - l) // 2)
            if n[m] < target: l = m + 1
            elif n[m] > target: r = m - 1
            else: return True
    return False