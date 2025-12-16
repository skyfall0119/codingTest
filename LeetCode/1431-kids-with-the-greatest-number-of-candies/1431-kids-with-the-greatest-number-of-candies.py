# import numpy as np
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # numpy
        # return ((np.array(candies) + extraCandies) >= np.max(candies)).tolist()

        # list comp
        return [c + extraCandies >= max(candies) for c in candies]
