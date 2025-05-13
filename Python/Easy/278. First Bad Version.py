def firstBadVersion(self, n: int) -> int:
    # Initial Solution
    # Time: O(log(n)) | Space: O(1)
    # Exceeds time limit with large inputs
    if n == 1 or isBadVersion(1): return 1
    l, r = 2, n + 1
    while True:
        m = l + (r - l) // 2
        m2_res = isBadVersion(m)
        if not m2_res:
            l = m
            continue
        m1_res = isBadVersion(m - 1) 
        if not m1_res: 
            return m
        r = m - 1