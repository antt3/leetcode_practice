def validPalindrome(self, s: str) -> bool:
    # Initial Solution
    # Time: O(n) | Space: O(1)
    skp_idx, side, l, r = -1, 0, 0, len(s) - 1
    while l < r:
        if (s[l] != s[r]):
            if not side:
                if s[l + 1] == s[r]: 
                    skp_idx = l
                    side = 1
                    l += 1
                elif s[l] == s[r - 1]:
                    side = 2
                    r -= 1
                else:
                    return False
            elif side == 1:
                l = skp_idx
                r = len(s) - skp_idx - 1
                if s[l] == s[r - 1]:
                    side = 2
                    r -= 1
                else:
                    return False
            else:
                return False
        l += 1
        r -= 1
    return True