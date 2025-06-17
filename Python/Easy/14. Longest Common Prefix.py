def longestCommonPrefix(self, strs: list[str]) -> str:
    # Initial Solution
    # Time: O(n * m) | Space: O(m)
    prefix = min(strs, key=len)
    for cur in strs:
        if not len(prefix):
            return prefix
        i = 0
        while i < len(prefix):
            if cur[i] != prefix[i]:
                prefix = prefix[:i]
            i += 1
    return prefix