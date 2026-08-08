class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeatA = ""
        count = 0

        while len(repeatA) < len(b):
            repeatA += a
            count += 1

        if b in repeatA:
            return count

        repeatA += a
        count += 1

        if b in repeatA:
            return count

        return -1