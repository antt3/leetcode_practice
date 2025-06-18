def longestCommonPrefix(self, strs: list[str]) -> str:
    # Improved Solution
    # Time: O(n * m) | Space: O(1)
    prefix = strs[0]
    for i in range(1, len(strs)):
        j = 0
        while j < min(len(prefix), len(strs[i])):
            if prefix[j] != strs[i][j]:
                break
            j += 1
        prefix = prefix[:j]
    return prefix
    
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