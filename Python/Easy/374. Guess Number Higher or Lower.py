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

    # Alternate Solution
    # Time: O(log3(n)) | Space: O(1)
    # l, r = 1, n
    # while True:
    #     m1 = l + (r - l) // 3
    #     m2 = r - (r - l) // 3
    #     if guess(m1) == 0:
    #         return m1
    #     if guess(m2) == 0:
    #         return m2
    #     if guess(m1) + guess(m2) == 0:
    #         l = m1 + 1
    #         r = m2 - 1
    #     elif guess(m1) == -1:
    #         r = m1 - 1
    #     else:
    #         l = m2 + 1