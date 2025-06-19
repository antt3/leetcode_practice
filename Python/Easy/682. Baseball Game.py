def calPoints(self, operations: list[str]) -> int:
    # My Improved Solution
    # Time: O(n) | Space: O(1)
    i = 0
    while i < len(operations):
        if operations[i] == "+":
            operations[i] = operations[i - 2] + operations[i - 1]
            i += 1
        elif operations[i] == "D":
            operations[i] = operations[i - 1] * 2
            i += 1
        elif operations[i] == "C":
            del operations[i]
            del operations[i - 1]
            i -= 1
        else:
            operations[i] = int(operations[i])
            i += 1
    return sum(operations)
    
    # Initial Solution
    # Time: O(n) | Space: O(n)
    # score = []
    # for v in operations:
    #     if v == "+":
    #         score.append(score[-2] + score[-1])
    #     elif v == "D":
    #         score.append(score[-1] * 2)
    #     elif v == "C":
    #         del score[-1]
    #     else:
    #         score.append(int(v))
    # return sum(score)