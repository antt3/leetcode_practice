class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            for j in range(i + 1, len(haystack) + 1):
                if haystack[i:j] == needle:
                    return i
        return -1

    # Best solution I found
    # def strStr(self, haystack, needle):
    #     # makes sure we don't iterate through a substring that is shorter than needle
    #     for i in range(len(haystack) - len(needle) + 1):
    #         # check if any substring of haystack with the same length as needle is equal to needle
    #         if haystack[i : i+len(needle)] == needle:
    #             # if yes, we return the first index of that substring
    #             return i
    #     # if we exit the loop, return -1        
    #     return -1

    # Fastest runtime, but uses try/except
    # def strStr(self, haystack: str, needle: str) -> int:
    #     try:
    #         return haystack.index(needle)
    #     except:
    #         return -1