def distributeCandies(self, candyType: list[int]) -> int:
    # Ideal Solution
    # Time: O(n) | Space O(n)
    return min(len(set(candyType)), len(candyType) // 2)

    # Improved Solution
    # Time: O(n) | Space O(n)
    # types = set()
    # for i in range(len(candyType)):
    #     types.add(candyType[i])
    # return len(types) if len(types) <= len(candyType) // 2 else len(candyType) // 2

    # Initial Solution
    # Time: O(n) | Space O(n)
    # types = set()
    # count = 0
    # i = 0
    # while i < len(candyType) and count < len(candyType) / 2:
    #     if candyType[i] not in types:
    #         types.add(candyType[i])
    #         count += 1
    #     i += 1
    # return count