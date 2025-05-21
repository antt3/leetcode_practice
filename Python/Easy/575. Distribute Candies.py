def distributeCandies(self, candyType: list[int]) -> int:
    types = set()
    count = 0
    i = 0
    while i < len(candyType) and count < len(candyType) / 2:
        if candyType[i] not in types:
            types.add(candyType[i])
            count += 1
        i += 1
    return count