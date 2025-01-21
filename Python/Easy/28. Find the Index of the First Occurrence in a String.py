class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            for j in range(i + 1, len(haystack) + 1):
                if haystack[i:j] == needle:
                    return i
        return -1

    # Fastest runtime, but uses try/except
    # def strStr(self, haystack: str, needle: str) -> int:
    #     try:
    #         return haystack.index(needle)
    #     except:
    #         return -1