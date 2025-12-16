class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sums = 0
        res = 0
        for i in range(len(gain)):
            sums += gain[i]
            res = max(sums, res)
        return res
