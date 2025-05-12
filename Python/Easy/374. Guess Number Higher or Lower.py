def guessNumber(self, n: int) -> int:
    # Initial Solution
    # Time: O(log(n)) | Space O(1)
    l, r = 0, n
    while l <= r:
        m = l + ((r - l) // 2)
        pick = guess(m)
        if pick == -1: r = m - 1
        elif pick == 1: l = m + 1
        else: return m