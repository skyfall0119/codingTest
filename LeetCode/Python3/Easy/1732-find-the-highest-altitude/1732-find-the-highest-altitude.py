class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        cur = 0

        for i in range(len(gain)):
            cur += gain[i]
            highest = max(highest, cur)

        return highest



