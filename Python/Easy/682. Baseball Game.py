def calPoints(self, operations: list[str]) -> int:
    # Initial Solution
    # Time: O(n) | Space: O(n)
    score = []
    for v in operations:
        if v == "+":
            score.append(score[-2] + score[-1])
        elif v == "D":
            score.append(score[-1] * 2)
        elif v == "C":
            del score[-1]
        else:
            score.append(int(v))
    return sum(score)